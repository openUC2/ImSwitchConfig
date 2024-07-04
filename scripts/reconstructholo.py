#%%
import numpy as np
import NanoImagingPack as nip
import matplotlib.pyplot as plt
import tifffile as tif
#%%

mImage = tif.imread('C://Users//T490//Documents//ImSwitch//imswitch//ImSwitch//recordings//2024-03-04//13h39m36s_snap_WidefieldCamera.tiff')

mImageFT = nip.ft(mImage)

plt.imshow(np.log(1+np.abs(mImageFT))), plt.show()


mCenter = (454,2242)
mSize = 300
mImageFTCrop = nip.extract(mImageFT, (mSize,mSize), mCenter, checkComplex=False)
mHolo = nip.ift(mImageFTCrop)

plt.figure(1);plt.imshow(np.abs(mHolo)); plt.show()
plt.figure(2);plt.imshow(np.angle(mHolo)); plt.show()


plt.imshow(np.log(1+np.abs(mImageFTCrop))), plt.show()