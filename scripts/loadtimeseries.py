import os
import tifffile

# Define the path to the top-level directory containing the subfolders
dir_path = r'C:\Users\user\Documents\ImSwitchConfig\recordings\2023_04_24-09-12-25_PM'
dir_path = r'C:\Users\user\Documents\ImSwitchConfig\recordings\2023_04_26-11-28-10_AM'
dir_path = r'C:\Users\user\Documents\ImSwitchConfig\recordings\2023_04_26-12-22-57_PM'
dir_path = r'C:\Users\user\Documents\ImSwitchConfig\recordings\2023_04_26-12-34-01_PM'

# Loop through each subfolder in sequence and load all TIF images
for i in range(60):  # assuming 10 subfolders numbered 0-9
    sub_dir = os.path.join(dir_path, "t"+str(i+1))  # get the path to the current subfolder
    for file_name in os.listdir(sub_dir):  # loop through all files in the subfolder
        if file_name.endswith('.tif'):  # check if the file is a TIF image
            file_path = os.path.join(sub_dir, file_name)  # get the full path to the TIF image
            tif_data = tifffile.imread(file_path)  # load the TIF image data
            # do something with the TIF data, e.g. print its shape
            print(f'TIF image {file_name} has shape {tif_data.shape}')
            tifffile.imwrite(dir_path+"stack.tif",tif_data, append=True)