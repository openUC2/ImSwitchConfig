import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

zpos = 7500
# x,y,z
maxX = 14000
minX = -192000
minY = -80000
maxY = 240000
positions = [	(maxX,maxY,zpos),
				(maxX,minY,zpos),
				(minY,minY,zpos),
				(minY,maxY,zpos)]
				
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
print("Start scanning")

iiter = 0
while 1:
	for position in positions:
		print(position)
		posX = position[0]
		api.imcontrol.movePositioner(positionerName, "X", posX, True, True)
		# Y
		posY = position[1]
		api.imcontrol.movePositioner(positionerName, "Y", posY, True, True)
		#Z
		posZ = position[2]
		api.imcontrol.movePositioner(positionerName, "Z", posZ, True, True)

		time.sleep(1)
		
		api.imcontrol.snapImage() 
	time.sleep(2*60)
	iiter +=1
	print(iiter)
	