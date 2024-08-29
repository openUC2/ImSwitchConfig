# Install: " git clone https://gitlab.com/openflexure/openflexure-stitching
# cd openflexure-stitching
# python -m pip install -r requirements.txt
# python -m install -e . --no-deps
# Importing necessary libraries
import numpy as np
import time
import os
from PIL import Image
from ashlar.scripts.ashlar import process_images
from pathlib import Path
import piexif
import json

# Constants and configuration
mPixelSize = 1.0  # micron - use a calibration chart to get this right!
input_dir = "./mScanImages"
output_dir = "./mStitchedImage"
input_name = "TmpTileFile.jpg"
output_name = "ResultingStitchedImage.jpg"
initialPosX = 0
initialPosY = 0
maximum_shift_microns = 1000
Nx = 2
Ny = 2
flip_x = True
flip_y = False

# Create the folders and names
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(output_dir).mkdir(parents=True, exist_ok=True)
ashlar_output_file = os.path.join(output_dir, output_name)
ashlar_input_file = os.path.join(input_dir, input_name)

# Define the frame shape, dimensions, and overlap
mFrameShape = api.imcontrol.snapImage(True, False).shape
xDim = mFrameShape[1] * mPixelSize
yDim = mFrameShape[0] * mPixelSize
mOverlap = 0.8  # 90% overlap at the edges

# Set the motor control to 0 and define the motor speeds for the X, Y, and Z axes
positionerName = api.imcontrol.getPositionerNames()[0]
api.imcontrol.setPositionerSpeed(positionerName, "X", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Y", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Z", 2000)

# Capture images in a grid pattern, save them with coordinates as the filename and add metadata
iiter = 0
mImageList = []
position_list = []
for ix in range(Nx):
    for iy in range(Ny):
        mPos = (ix * xDim * mOverlap + initialPosX, iy * yDim * mOverlap + initialPosY)
        api.imcontrol.movePositioner(positionerName, "XY", mPos, True, True)
        time.sleep(0.5)
        mFrame = api.imcontrol.snapImage(True, False)
        
        # Convert to 8-bit grayscale
        if mFrame.dtype != np.uint8:
            mFrame = (mFrame / np.max(mFrame) * 255).astype(np.uint8)
        
        # Prepare metadata for EXIF
        user_comment = json.dumps({
            'instrument': {
                'state': {'stage': {'position': {'x': mPos[0], 'y': mPos[1]}}},
                'settings': {'extensions': {
                    'org.openflexure.camera_stage_mapping': {
                        'image_to_stage_displacement': [[1, 0], [0, 1]]
                    }
                }}
            }
        }).encode('utf-8')
        
        exif_dict = {
            "Exif": {
                piexif.ExifIFD.UserComment: user_comment
            }
        }
        exif_bytes = piexif.dump(exif_dict)
        
        # Save image with metadata
        img_filename = f"{input_dir}/image_{ix}_{iy}.jpg"
        image = Image.fromarray(mFrame, mode='L')
        image.save(img_filename, "JPEG", exif=exif_bytes)
        
        mImageList.append(mFrame)
        position_list.append(mPos)
        print(mPos)
        
        iiter += 1

		
# Importing necessary libraries and functions
import numpy as np
import os
import json
import piexif
from PIL import Image
from pathlib import Path
#from typing import Optional, List
#from argparse import Namespace
#from openflexure_stitching.loading import load_images
#from openflexure_stitching.correlation import correlate_overlapping_images
from openflexure_stitching.types import CorrelationSettings, TilingSettings, PairData
from openflexure_stitching.pipeline import load_tile_and_stitch
#from openflexure_stitching. import plotting
#from openflexure_stitching.optimisation import test_all_thresholds, filter_pairs, fit_positions_lstsq, manual_threshold
#from openflexure_stitching.stitching import stitch_and_save, stitch_to_tiles
#from openflexure_stitching.loading import get_img_size

try:
    from openflexure_stitching.stitching.pyramidal_tiff import produce_tiff
    TIFF_ENABLED = True
except ImportError:
    print("VIPS not installed: TIFF export disabled")
    TIFF_ENABLED = False

# Constants and configuration
stitching_mode = "all"  # Options: 'all', 'only_correlate', 'only_stage_stitch'
stitch_tiff = False  # Set to True if you want to produce a pyramidal TIFF

correlation_settings = CorrelationSettings(
    pad=True,
    resize=0.5,
    high_pass_sigma=50,
    minimum_overlap=0.29,
    priority="time"
)

tiling_settings = TilingSettings(
    csm_matrix=[[0, 0], [0, 0]],  # This would typically be loaded from your images
    csm_calibration_width=-1,
    thresholding_method="automatic"
)

# Creating necessary directories and preparing images
input_dir = "./mScanImages"
output_dir = "./mStitchedImage"

# Now directly calling the load_tile_and_stitch function
load_tile_and_stitch(
    folder=input_dir,
    correlation_settings=correlation_settings,
    tiling_settings=tiling_settings,
    stitching_mode=stitching_mode,
    stitch_tiff=stitch_tiff
)

		