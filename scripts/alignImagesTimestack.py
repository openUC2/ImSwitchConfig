# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 13:03:16 2023

@author: user
"""

import scipy
import numpy as np
import os
import tifffile as tif
from scipy.ndimage import fourier_shift
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
from skimage.registration import phase_cross_correlation

import scipy.signal as signal

import skimage.transform as transform
import matplotlib.pyplot as plt

def downscale_image(image, factor):
    # Downscale the image
    downscaled_image = transform.downscale_local_mean(image, (factor, factor))

    return downscaled_image


def crop_center(image, size):
    # Get the dimensions of the image
    height, width = image.shape[:2]

    # Calculate the coordinates for cropping
    start_x = max(0, int((width - size) / 2))
    start_y = max(0, int((height - size) / 2))
    end_x = min(width, start_x + size)
    end_y = min(height, start_y + size)

    # Crop the image
    cropped_image = image[start_y:end_y, start_x:end_x]

    return cropped_image


factor = 5
cropSize = 800
iShift = [0,0]
for i in range(1,100):
    # Directory containing the image files
    directory = 'C:\\Users\\user\\Documents\\ImSwitchConfig\\recordings\\2023_07_11-03-54-59_PM\\t'+str(i)
    
    # Initialize empty dictionaries for each laser

    imageList = []
    led_images = []
    
    os.chdir(directory)
    
    # Read image files and store them in the corresponding dictionary
    for filename in sorted(os.listdir(directory), key=os.path.getmtime):
        if filename.endswith('.tif'):
            if 'Laser2' in filename:
                image_path = os.path.join(directory, filename)
                image = tif.imread(image_path)
                image = crop_center(image, cropSize)
                image = downscale_image(image, factor)

                imageList.append(image)
                
    # Find max focus 
    bestFocus = 0
    bestFocusIndex = 0
    for index,image in enumerate(imageList):
        imagearraygf = ndi.filters.gaussian_filter(image, 3)

        # 3 compute focus metric
        focusValue = np.mean(ndi.filters.laplace(imagearraygf))
        if focusValue > bestFocus:
            bestFocus = focusValue
            bestFocusIndex = index

    # Align the images
    image2 = np.std(imageList, (0))
    
    #image2 = scipy.ndimage.gaussian_filter(image2, sigma=10)
    if i>1:
        shift, error, diffphase = phase_cross_correlation(image1, image2)
        iShift += (shift)
        
        # Shift image2 to align with image1
        image = imageList[bestFocusIndex]
        aligned_image = np.roll(image, int(iShift[1]), axis=1)
        aligned_image = np.roll(aligned_image,int(iShift[0]), axis=0)
        

        
        print(f'Known offset (y, x): {shift*factor}')

        # Display the aligned image
        plt.imshow(aligned_image)
        plt.axis('off')
        plt.show()
   
    image1 = image2.copy()

    

            