import numpy as np
import time

#mainWindow.setCurrentModule('imcontrol')

laserNameR = "635 Laser"
laserNameB = "488 Laser"
ledName = "LED"


iiter = 0
tperiode=1 #minuten
isautofocus=False


while True:
	print(iiter)
	api.imcontrol.setLaserActive(ledName, True)
	api.imcontrol.snapImage()
	
	time.sleep(tperiode*60)
	iiter +=1
	
