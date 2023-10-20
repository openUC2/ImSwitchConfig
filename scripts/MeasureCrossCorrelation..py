
from skimage.registration import phase_cross_correlation
import time
import cv2
import tifffile as tif
import numpy as np
# Reduce dimensions by a factor of 10

image1 = None
image2 = None	

positionerName = api.imcontrol.getPositionerNames()[0]
positions = api.imcontrol.getPositionerPositions()

posXinit = positions["ESP32Stage"]["X"]


def preProcess(inputImage):
		scale_factor = 1/2
		inputImage_ = cropCenter(np.copy(inputImage), crop_size=512)
		inputImage_ = cv2.resize(inputImage_, None, fx=scale_factor, fy=scale_factor)
		# Apply Gaussian blur
		kernel_size = (5, 5)  # Adjust the kernel size as needed
		inputImage_ = cv2.GaussianBlur(inputImage_, kernel_size, 0)
		return inputImage_
		
def cropCenter(marray, crop_size=512):
	center_x, center_y = marray.shape[1] // 2, marray.shape[0] // 2

	# Calculate the starting and ending indices for cropping
	x_start = center_x - crop_size // 2
	x_end = x_start + crop_size
	y_start = center_y - crop_size // 2
	y_end = y_start + crop_size

	# Crop the center region
	return marray[y_start:y_end, x_start:x_end]

	
iiter = 0
backgroundImage = []
while 1:

	iiter +=1
	
	image2 = api.imcontrol.snapImage(True, False)
	
	
	if iiter >10:	
		
		if type(backgroundImage)==list:
			backgroundImage = np.array(backgroundImage)
			backgroundImage = np.mean(backgroundImage,0)
			backgroundImage = preProcess(backgroundImage)
			print(backgroundImage.shape)
		# normalization
		image1_ = preProcess(image1)/backgroundImage
		image2_ = preProcess(image2)/backgroundImage
		image1_ = np.uint8(image1_/np.max(image1_)*255)
		image2_ = np.uint8(image2_/np.max(image2_)*255)
		
		
		shift, error, diffphase = phase_cross_correlation(image1_, image2_)
		print(f"Shift (x, y) and motion: ({shift[0]}, {shift[1]}, {posX}, {shift[1]/posX}) pixels")

		

		
		tif.imwrite("test9.tif", np.hstack((image1_,image2_)), append=True)
	else:
		backgroundImage.append(image2)

	if iiter <10:
		posX = posXinit + np.random.randint(100)-50
		api.imcontrol.movePositioner(positionerName, "Y", posX, True, True)
	else:
		posX = (iiter // 10 % 2 -.5)*20
		api.imcontrol.movePositioner(positionerName, "Y", posX, False, True)
		
	image1 = np.copy(image2)
	

	
	
	time.sleep(0.5)
