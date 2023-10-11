import numpy as np
import time
import threading 
mainWindow.setCurrentModule('imcontrol')

api.imcontrol.enalbeMotors(None, False)
# x,y,z
positions = [	(0, 80000, -4290),
				(17000, 80000, -4340),
				(17000, 96000, -4290),
				(9000, 96000, -4290)]
positions = [(9000, 7000, 110),
				(18000, 16000, 110),
				(54000, 25000, -130),
				(63000, 52000, -240)]

positionerName = api.imcontrol.getPositionerNames()[0]
print(api.imcontrol.getPositionerPositions())
api.imcontrol.setPositionerSpeed(positionerName, "X", 25000)
api.imcontrol.setPositionerSpeed(positionerName, "Y", 25000)
api.imcontrol.setPositionerSpeed(positionerName, "Z", 25000)

api.imcontrol.homeAxis(positionerName, "X")
api.imcontrol.homeAxis(positionerName, "Y")
time.sleep(15)
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
def doScanning():
	iiter = 0
	while 1:
		iPos = 0
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
			
			api.imcontrol.snapImageToPath(str(iPos)+"_posscreening") 
			iPos +=1
		time.sleep(60)
		iiter +=1
		print(iiter)

doScanning()

