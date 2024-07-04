		
# Importing necessary libraries and functions
from PIL import Image
from pathlib import Path
from openflexure_stitching.types import CorrelationSettings, TilingSettings, PairData
from openflexure_stitching.pipeline import load_tile_and_stitch

try:
    from openflexure_stitching.stitching.pyramidal_tiff import produce_tiff
    TIFF_ENABLED = True
except ImportError:
    print("VIPS not installed: TIFF export disabled")
    TIFF_ENABLED = False

# Constants and configuration
stitching_mode = "all"  # Options: 'all', 'only_correlate', 'only_stage_stitch'
stitch_tiff = TIFF_ENABLED  # Set to True if you want to produce a pyramidal TIFF

correlation_settings = CorrelationSettings(
    pad=True,
    resize=0.5,
    high_pass_sigma=50,
    minimum_overlap=0.29,
    priority="time"
)

CSMMatrix = [[0.0,-1.0013599686228887],
            [-1.0013599686228885,0.0]]
#[[0, 1], [1, 0]]
tiling_settings = TilingSettings(
    csm_matrix=CSMMatrix,  # This would typically be loaded from your images
    csm_calibration_width=-1,
    thresholding_method="automatic"
)

# Creating necessary directories and preparing images
input_dir = "/Users/bene/Dropbox/Dokumente/Promotion/PROJECTS/MicronController/ImSwitch/mScanImages"

# Now directly calling the load_tile_and_stitch function
load_tile_and_stitch(
    folder=input_dir,
    correlation_settings=correlation_settings,
    tiling_settings=tiling_settings,
    stitching_mode=stitching_mode,
    stitch_tiff=stitch_tiff
)

		