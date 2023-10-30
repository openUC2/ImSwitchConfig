import numpy as np
import time

#mainWindow.setCurrentModule('imcontrol')

positionerName = api.imcontrol.getPositionerNames()[0]
initialPosition = api.imcontrol.getPositionerPositions()[positionerName]

# x,y,z
root1 = (0,0,initialPosition["Z"])
root2 = (1000,0,initialPosition["Z"])
root3 = (5000,300,initialPosition["Z"])


rootPositions = (root1, root2, root3)


Pos1 = (44000, -65000, 8500)
Pos2 = (32500, -65000, 8500)
Pos3 = (26000, -65000, 8300)
Pos4 = (19000, -65900, 8200)
Pos5 = (14500, -66900, 8200)
	
rootPositions = (Pos1, Pos2, Pos3, Pos4, Pos5)
	
for iPosition in rootPositions:
	# move to individual positions 
	posX = iPosition[0]
	# positionerName, axis, steps, absolute?, blocking?)
	api.imcontrol.movePositioner(positionerName, "X", posX, True, True)
	# Y
	posY = iPosition[1]
	api.imcontrol.movePositioner(positionerName, "Y", posY, True, True)
	#Z
	posZ = iPosition[2]
	api.imcontrol.movePositioner(positionerName, "Z", posZ, True, True)
	
	if 0:
		# move along the root 
		for iY in range(5):
			#relative motion along y 
			api.imcontrol.movePositioner(positionerName, "Y", 100, False, True)
			api.imcontrol.snapImageToPath("iY"+str(iY))
		api.imcontrol.movePositioner(positionerName, "Y", posY, True, True)	
	