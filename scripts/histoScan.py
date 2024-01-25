import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

# x,y,z
initPos = api.imcontrol.getPositionerPositions()["ESP32Stage"]
initPos = (initPos["X"],initPos["Y"],initPos["Z"])
nPixels = (3072,2048)
pixelSize = 0.225
overlap = 0.8
posZ = initPos[-1]
positionerName = api.imcontrol.getPositionerNames()[0]
print(api.imcontrol.getPositionerPositions())

nX = 10
nY = 10

positionList = []
for iy in range(nY):
	for ix in range(nX):

		posX = ix * pixelSize*nPixels[0]*overlap+initPos[0]
		posY = iy * pixelSize*nPixels[1]*overlap+initPos[1]
		api.imcontrol.movePositioner(positionerName, "XY", (posX, posY), True, True)
		print(str(posX)+"-"+str(posY))
		time.sleep(.2)
		api.imcontrol.snapImageToPath(str((posX,posY)))
		positionList.append((posX, posY, posZ))


posX = initPos[0]
posY = initPos[1]
api.imcontrol.movePositioner(positionerName, "XY", (posX, posY), True, True)

np.save("positions", positionList)
		
				