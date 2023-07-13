import numpy as np
import os
import tifffile as tif

import scipy.ndimage as ndi
import matplotlib.pyplot as plt


for i in range(1,100):
    # Directory containing the image files
    directory = 'C:\\Users\\user\\Documents\\ImSwitchConfig\\recordings\\2023_07_11-03-54-59_PM\\t'+str(i)
    
    # Initialize empty dictionaries for each laser
    laser1_images = []
    laser2_images = []
    led_images = []
    
    os.chdir(directory)
    
    # Read image files and store them in the corresponding dictionary
    for filename in sorted(os.listdir(directory), key=os.path.getmtime):
        if filename.endswith('.tif'):
            if 'Laser1' in filename:
                image_index = int(filename.split('_i_')[1].split('_Z_')[0])
                image_path = os.path.join(directory, filename)
                image = tif.imread(image_path)
                laser1_images.append(image)
                plt.imshow(image), plt.show()
            elif 'Laser2' in filename:
                image_index = int(filename.split('_i_')[1].split('_Z_')[0])
                image_path = os.path.join(directory, filename)
                image = tif.imread(image_path)
                laser2_images.append(image)
            elif 'LED' in filename:
                image_index = int(filename.split('_i_')[1].split('_Z_')[0])
                image_path = os.path.join(directory, filename)
                image = tif.imread(image_path)
                led_images.append(image)
    
    #%%
    # Measure the variation of each image stack
    resultList = []
    index=0
    for imageList in (laser1_images, laser2_images, led_images):
        variation=[]
        for image in imageList:
            imagearraygf = ndi.filters.gaussian_filter(image, 3)
    
            # 3 compute focus metric
            focusValue = np.mean(ndi.filters.laplace(imagearraygf))
            variation.append(focusValue)
            
        plt.plot(variation), plt.show()
        inFocusImage = imageList[np.argmax(variation)]
        resultList.append(inFocusImage)
        tif.imsave("C:\\Users\\user\\Documents\\ImSwitchConfig\\recordings\\2023_07_11-03-54-59_PM\\"+"result_"+str(index)+".tif", inFocusImage, append=True)
        plt.imshow(inFocusImage), plt.show()
        index+=1
        
# %% align data