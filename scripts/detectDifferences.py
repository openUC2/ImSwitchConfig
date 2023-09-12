import numpy as np
import time
from skimage.metrics import structural_similarity as ssim
import cv2

mainWindow.setCurrentModule('imcontrol')

laserName = "635 Laser"
ledName = "488 Laser"
laserName = "LED"

iiter = 1

def compute_ssim(imageA, imageB):
    # Ensure the images are the same size
    assert imageA.shape == imageB.shape, "Images must have the same dimensions."

    # Compute SSIM between two images
    return ssim(imageA, imageB)

mImage1 = api.imcontrol.snapImage(True, False)


		
while True:
	#laser = api.imcontrol.setLaserActive(laserName, True)
	time.sleep(2)
	
	mImage2 = api.imcontrol.snapImage(True, False)
	print(np.mean(mImage2-mImage1))
	similarity_index = compute_ssim(mImage1, mImage2)
	print("SSIM:", similarity_index)

	#mImage1 = np.copy(mImage2)
