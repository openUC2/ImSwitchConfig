import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

laserName = "LED"

iiter = 1

#positioner = api.imcontrol.getPositionerNames()
while True:
	api.imcontrol.setLaserActive(laserName, True)
	time.sleep(1)
	api.imcontrol.snapImage() 
	api.imcontrol.setLaserActive(laserName, False)

	time.sleep(1*60)
	print(iiter)
	iiter +=1