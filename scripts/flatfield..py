#%%
import numpy as np
import tifffile as tif
import NanoImagingPack as nip
import napari
mImage = tif.imread('/Users/bene/Dropbox/2023_02_23-02-35-26_PM Manuel_Composite_Niceresult.tif')


#tif.imwrite("test.tif", )
# %%
#flatfield
mImage = mImage/np.expand_dims(np.expand_dims(np.mean(mImage, (2,3)),-1),-1)
mImage /= np.expand_dims(nip.gaussf(np.mean(mImage, 0),25),0)
                             
#%%        
viewer = napari.view_image(
        nip.gaussf(mImage,1),
        channel_axis=1,
        name=["membrane", "nuclei"],
        colormap=["green", "magenta"],
        contrast_limits=[[0, 5], [0, 5]],
        scale=[3,1,1]
        )
# %%
