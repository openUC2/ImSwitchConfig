import numpy as np
import time
import numpy as np
import scipy.ndimage as ndi

mainWindow.setCurrentModule('imcontrol')

ledName = "LED"
laserNameB = "488 Laser"

laserNameR = "635 Laser"

iiter = 0
tperiode=0.1 #minuten
isautofocus=False


def cropCenter(marray, crop_size=512):
	center_x, center_y = marray.shape[1] // 2, marray.shape[0] // 2

	# Calculate the starting and ending indices for cropping
	x_start = center_x - crop_size // 2
	x_end = x_start + crop_size
	y_start = center_y - crop_size // 2
	y_end = y_start + crop_size

	# Crop the center region
	return marray[y_start:y_end, x_start:x_end]

	
positionerName = api.imcontrol.getPositionerNames()[0]
positions = api.imcontrol.getPositionerPositions()

posZinit = positions["ESP32Stage"]["Z"]
print(posZinit)

api.imcontrol.movePositioner(positionerName, "Z", -100, False, True)
	
allfocusvals = []
for i in range(20):
	api.imcontrol.setLaserActive(laserNameB, True)
	time.sleep(.3)
	mImage = api.imcontrol.snapImage(True, False)
	api.imcontrol.setLaserActive(laserNameB, False)
	
	# 2 Gaussian filter the image, to remove noise
	mImage = cropCenter(mImage, crop_size=1024)
	# img_norm = img-np.min(img)
	# img_norm = img_norm/np.mean(img_norm)
	imagearraygf = ndi.filters.gaussian_filter(mImage, 3)

	# 3 compute focus metric
	focusquality = np.mean(ndi.filters.laplace(imagearraygf))
	allfocusvals.append(focusquality)
	
	print(focusquality)
		
	api.imcontrol.movePositioner(positionerName, "Z", 10, False, True)
	time.sleep(.1)
	
api.imcontrol.movePositioner(positionerName, "Z", posZinit, True, True)
