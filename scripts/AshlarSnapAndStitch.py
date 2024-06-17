# install the library ( we use the modified version from openuc2 that also enables the use of casehd numpy arrays)
# do: python -m pip install https://github.com/openuc2/ashlar

# importing necessary libraries
mainWindow.setCurrentModule('imcontrol')
import numpy as np
import time
import threading
import os
import tifffile
import re
from ashlar.scripts import ashlar
from ashlar.scripts.ashlar import process_images
from pathlib import Path

# Calculate the image size and the overlap of the images based on pixel size and resolution.
mPixelSize = 1.0  # micron - use a calibration chart to get this right!
input_dir = "./mScanImages"
output_dir = "./mStitchedImage"
input_name = "TmpTileFile.ome.tif"
output_name = "ResultingStitchedImage.ome.tif"
initialPosX = 0
initialPosY = 0
maximum_shift_microns = 1000
Nx = 5
Ny = 5
# please try changing these two values to make it match!
flip_x=True
flip_y=False

# create the folders and names
Path(input_dir).mkdir(parents=True, exist_ok=True)
Path(output_dir).mkdir(parents=True, exist_ok=True)
ashlar_output_file = os.path.join(output_dir, output_name)
ashlar_input_file = os.path.join(input_dir, input_name)

mFrameShape = api.imcontrol.snapImage(True, False).shape
xDim = mFrameShape[1] * mPixelSize
yDim = mFrameShape[0] * mPixelSize
mOverlap = 0.8  # 90% overlap at the edges

# Set the motor control to 0 and define the motor speeds for the X, Y, and Z axes.
positionerName = api.imcontrol.getPositionerNames()[0]
api.imcontrol.setPositionerSpeed(positionerName, "X", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Y", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Z", 2000)

## Capture images in a 2x3 grid pattern. The stage moves to the start position and captures images at each step. Each image is saved with coordinates as the filename.
iiter = 0

USE_OME = False
if USE_OME:# on MAC ARM M1 it may not work..
    with tifffile.TiffWriter(input_name) as tif: ## Define the input and output directories, and the pixel size. Open a new TIFF file to write the collected tiles, read each image, extract the position from the filename, prepare metadata, and write the image with metadata into the TIFF file. Finally, use ASHLAR to stitch the images together.
        for ix in np.arange(Nx):
            for iy in np.arange(Ny):
                mPos = (ix * xDim * mOverlap + initialPosX, iy * yDim * mOverlap + initialPosY)
                api.imcontrol.movePositioner(positionerName, "XY", mPos, True, True)
                time.sleep(0.5)
                mFrame = api.imcontrol.snapImage(True, False)
                metadata = {
				  'Pixels': {'PhysicalSizeX': mPixelSize, 'PhysicalSizeXUnit': 'm', 'PhysicalSizeY': mPixelSize, 'PhysicalSizeYUnit': 'm'},
				  'Plane': {'PositionX': ix, 'PositionY': iy}
			 	}
                tif.write(mFrame, metadata=metadata)
                iiter += 1
    ashlar.main(['', ashlar_input_file, '-o', ashlar_output_file, '--pyramid', '-m%s' % maximum_shift_microns, "-flip_x", flip_x, "-flip_y", flip_y])
	
else: # this is a workaround with a numpy reader instead
	mImageList = []
	position_list = [] 
	for ix in range(Nx):
		for iy in range(Ny):
			mPos = (ix * xDim * mOverlap + initialPosX, iy * yDim * mOverlap + initialPosY)
			api.imcontrol.movePositioner(positionerName, "XY", mPos, True, True)
			time.sleep(0.5)
			mFrame = api.imcontrol.snapImage(True, False)
			mImageList.append(mFrame)
			position_list.append(mPos)
			print(mPos)
	arrays = [np.expand_dims(np.array(mImageList),1)]  # (num_images, num_channels, height, width)
	# create a 2D list of xy positions 
	position_list = np.array(position_list)

	# Process numpy arrays
	process_images(filepaths=arrays,
					output='ashlar_output.tif',
					align_channel=0,
					flip_x=flip_x,
					flip_y=flip_y,
					flip_mosaic_x=False,
					flip_mosaic_y=False,
					output_channels=None,
					maximum_shift=maximum_shift_microns,
					stitch_alpha=0.01,
					maximum_error=None,
					filter_sigma=0,
					filename_format='cycle_{cycle}_channel_{channel}.tif',
					pyramid=False,
					tile_size=1024,
					ffp=None,
					dfp=None,
					barrel_correction=0,
					plates=False,
					quiet=False, 
					position_list=position_list,
					pixel_size=mPixelSize)
	mImage = tifffile.imread('ashlar_output.tif')
	
	#display the resulting tiles
	api.imcontrol.displayImageNapari("Tiles", arrays[0], isRGB=False)	
	
	print(position_list)
	# display the resulting image
	api.imcontrol.displayImageNapari("StitchedImage", mImage, isRGB=False)