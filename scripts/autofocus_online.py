import numpy as np
import time
import numpy as np
import scipy.ndimage as ndi
import tifffile as tif
from skimage.filters import gaussian, median


mainWindow.setCurrentModule('imcontrol')

ledName = "LED"
laserNameB = "488 Laser"

laserNameR = "635 Laser"



def cropCenter(marray, crop_size=512):
	center_x, center_y = marray.shape[1] // 2, marray.shape[0] // 2

	# Calculate the starting and ending indices for cropping
	x_start = center_x - crop_size // 2
	x_end = x_start + crop_size
	y_start = center_y - crop_size // 2
	y_end = y_start + crop_size

	# Crop the center region
	return marray[y_start:y_end, x_start:x_end]

def measureFocus(mImage, nGauss=5):
	# 2 Gaussian filter the image, to remove noise
	mImage = cropCenter(mImage, crop_size=1024)
	# img_norm = img-np.min(img)
	# img_norm = img_norm/np.mean(img_norm)
	imagearraygf = ndi.filters.gaussian_filter(mImage, nGauss)

	# 3 compute focus metric
	mLaplace = ndi.filters.laplace(imagearraygf)
	focusquality = np.mean(mLaplace)
	return focusquality, mLaplace

def recordFlatfield(nFrames=10, nGauss=16):
	flatfield = []
	for iFrame in range(nFrames):
		mFrame = api.imcontrol.snapImage(True, False)
		flatfield.append(mFrame)
	flatfield = np.mean(np.array(flatfield),0)
	# normalize and smooth using scikit image
	flatfield = gaussian(flatfield, sigma=nGauss)
	#flatfield = median(flatfield, selem=np.ones((nMedian, nMedian)))
	return flatfield

positionerName = api.imcontrol.getPositionerNames()[0]
positionsStart = api.imcontrol.getPositionerPositions()
posZstart = positionsStart["ESP32Stage"]["Z"]
print(posZstart)

# record flatfield in out-of-focus state
dDefocus = 500
api.imcontrol.movePositioner(positionerName, "Z", -dDefocus, False, True)
time.sleep(1)
flatfieldFrame = recordFlatfield()
api.imcontrol.movePositioner(positionerName, "Z", posZstart, True, True)
time.sleep(1)
# 
dz = 50
tPause = 20

for i in range(100):
	positions = api.imcontrol.getPositionerPositions()
	posZinit = positions["ESP32Stage"]["Z"]
	
	allFocusVal = []
	allFocusPositions = np.linspace(-dz,dz,5)
	for iZ in allFocusPositions:
		api.imcontrol.movePositioner(positionerName, "Z", posZinit + iZ, True, True)
		time.sleep(1)
		mImage = api.imcontrol.snapImage(True, False)/flatfieldFrame
		
		focusquality, mLaplace = measureFocus(mImage, 7)
		allFocusVal.append(focusquality)
		tif.imsave("laplace4.tif", mLaplace, append=True)
	allFocusVal = np.array(allFocusVal)
	print(allFocusVal)
	focusIndex = np.argmax(allFocusVal)
	print(focusIndex)
	bestFocusPos = allFocusPositions[focusIndex]

	#api.imcontrol.movePositioner(positionerName, "Z", posZstart, True, True)
	api.imcontrol.movePositioner(positionerName, "Z", posZinit+bestFocusPos, True, True)
	time.sleep(1)
	mImage = api.imcontrol.snapImage(True, False)/flatfieldFrame
		
	tif.imsave("result2.tif", mImage, append=True)
	
	time.sleep(10)