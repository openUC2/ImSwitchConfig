import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

ledName = "LED"
laserNameB = "488 Laser"

laserNameR = "635 Laser"

iiter = 0
tperiode=0.5 #minuten
isautofocus=False


while True:
	print(iiter)
	api.imcontrol.setLaserActive(laserNameB, True)
	time.sleep(.3)
	api.imcontrol.snapImage()
	api.imcontrol.setLaserActive(laserNameB, False)
	time.sleep(1)
	api.imcontrol.setLaserActive(laserNameR, True)
	time.sleep(.3)
	api.imcontrol.snapImage()
	api.imcontrol.setLaserActive(laserNameR, False)
		
	time.sleep(tperiode*60)
	iiter +=1
	if iiter >120:
		break
	
