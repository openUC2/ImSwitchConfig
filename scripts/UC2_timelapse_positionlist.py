import numpy as np
import time

#mainWindow.setCurrentModule('imcontrol')




# x,y,z
positions = [	(0,0,1110),
				(0,14000,1110),
				(14000,14000,1110),
				(14000,0,1110),
				(28000,0,1110),
				(28000,14000,1110),
				(42000,14000,1110),
				(42000,0,1110)]
				
positionerName = api.imcontrol.getPositionerNames()[0]
print(api.imcontrol.getPositionerPositions())

# move to inital position
# X
position = positions[0]
posX = position[0]
api.imcontrol.movePositioner(positionerName, "X", posX, True, True)
# Y
posY = position[1]
api.imcontrol.movePositioner(positionerName, "Y", posY, True, True)
#Z
posZ = position[2]
api.imcontrol.movePositioner(positionerName, "Z", posZ, True, True)


#

iiter = 0
while 1:
	for position in positions:
		print(position)
		posX = position[0]
		api.imcontrol.movePositioner(positionerName, "X", posX, True)
		# Y
		posY = position[1]
		api.imcontrol.movePositioner(positionerName, "Y", posY, True)
		#Z
		posZ = position[2]
		api.imcontrol.movePositioner(positionerName, "Z", posZ, True)

		time.sleep(1)
		
		api.imcontrol.snapImage() 
	time.sleep(2*60)
	iiter +=1
	print(iiter)
	