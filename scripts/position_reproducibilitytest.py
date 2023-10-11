import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

dx = 10000
dy = 10000

positionerName = api.imcontrol.getPositionerNames()[0]
cX = api.imcontrol.getPositionerPositions()[positionerName]['X']
cY = api.imcontrol.getPositionerPositions()[positionerName]['Y']

api.imcontrol.setPositionerSpeed(positionerName, 'X', 20000)
api.imcontrol.setPositionerSpeed(positionerName, 'Y', 20000)
iiter=0
for i in range(5):
	# pos 1 
	api.imcontrol.movePositioner(positionerName, "X", cX, True,True)
	api.imcontrol.movePositioner(positionerName, "Y", cY, True,True)
	api.imcontrol.snapImageToPath("_1_"+str(iiter))
	# pos 2
	api.imcontrol.movePositioner(positionerName, "X", cX+dx, True,True)
	api.imcontrol.movePositioner(positionerName, "Y", cY, True,True)
	api.imcontrol.snapImageToPath("_2_"+str(iiter))
	# pos 3
	api.imcontrol.movePositioner(positionerName, "X", cX+dx, True,True)
	api.imcontrol.movePositioner(positionerName, "Y", cY+dy, True,True)
	api.imcontrol.snapImageToPath("_3_"+str(iiter))
	# pos 4 
	api.imcontrol.movePositioner(positionerName, "X", cX, True,True)
	api.imcontrol.movePositioner(positionerName, "Y", cY+dy, True,True)
	api.imcontrol.snapImageToPath("_4_"+str(iiter))
	time.sleep(1)