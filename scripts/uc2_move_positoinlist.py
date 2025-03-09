import numpy as np
import time
import threading
import os
import cv2
import tifffile as tif
#mainWindow.setCurrentModule('imcontrol')

api.imcontrol.enalbeMotors(None, False)

positionerName = api.imcontrol.getPositionerNames()[0]
print(api.imcontrol.getPositionerPositions())
api.imcontrol.setPositionerSpeed(positionerName, "X", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Y", 20000)
api.imcontrol.setPositionerSpeed(positionerName, "Z", 2000)

#api.imcontrol.homeAxis(positionerName, "X")
#api.imcontrol.homeAxis(positionerName, "Y")
#time.sleep(15)
# move to inital position

mPixelSize = 0.327 # mum
mFrameShape = api.imcontrol.snapImage(True, False).shape

xDim = mFrameShape[1]*mPixelSize
yDim = mFrameShape[0]*mPixelSize
mOverlap = 0.9 # 90% overlap at  the edges

print(xDim)
print(yDim)
mPath = r"C:\\Users\\T490\\Documents\\Anabel\\Bachelorarbeit\\Bilder\\Raster\\"
LEDName = "LED"
api.imcontrol.setLaserValue(LEDName, 1023)
api.imcontrol.setLaserActive(LEDName, True)
time.sleep(0.5)
#a record dummy frame
ix=iy=0
mPos = (ix*xDim*mOverlap+57000,
iy*yDim*mOverlap+30000)
api.imcontrol.movePositioner(positionerName, "XY", mPos, True, True)
mFrame = api.imcontrol.snapImage(True, False)

#raster
iiter = 0
for ix in range(2):
	for iy in range(2):
		mPos = (ix*xDim*mOverlap+57000,
		iy*yDim*mOverlap+30000)
		api.imcontrol.movePositioner(positionerName, "XY", mPos, True, True)
		time.sleep(0.5)
		# api.imcontrol.snapImageToPath(str(ix)+"_"+str(iy))
		mFrame = api.imcontrol.snapImage(True, False)
		tif.imsave(mPath+str(iiter)+"_("+str(int(mPos[0]))+", "+str(int(mPos[1]))+")"+".tif", mFrame)
		iiter +=1

caputure_and_save_images()

