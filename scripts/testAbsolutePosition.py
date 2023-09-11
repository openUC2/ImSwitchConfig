mainWindow.setCurrentModule('imcontrol')

positionerName = api.imcontrol.getPositionerNames()[0]
positionsStart = api.imcontrol.getPositionerPositions()
posZstart = positionsStart["ESP32Stage"]["Z"]
print(posZstart)

# 
dz = 20
tPause = 20
for i in range(5):

	api.imcontrol.movePositioner(positionerName, "Z", posZstart + 100, True, True)
	positions = api.imcontrol.getPositionerPositions()
	posZinit = positions["ESP32Stage"]["Z"]
	print(posZinit)

	api.imcontrol.movePositioner(positionerName, "Z", posZstart -100, True, True)	
	positions = api.imcontrol.getPositionerPositions()
	posZinit = positions["ESP32Stage"]["Z"]
	print(posZinit)

api.imcontrol.movePositioner(positionerName, "Z", posZstart, True, True)	
