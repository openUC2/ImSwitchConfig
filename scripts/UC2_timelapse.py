import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

laserName = "635 Laser"
ledName = "488 Laser"
laserName = "LED"

iiter = 1

#positioner = api.imcontrol.getPositionerNames()
while True:
	#laser = api.imcontrol.setLaserActive(laserName, True)
	#time.sleep(1)
	api.imcontrol.snapImage() 
	#laser = api.imcontrol.setLaserActive(laserName, False)

	time.sleep(.5*60)
	print(iiter)
	iiter +=1