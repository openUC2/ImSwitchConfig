import numpy as np
import time

#mainWindow.setCurrentModule('imcontrol')

laserNameR = "635 Laser"
laserNameB = "488 Laser"

ledName = "White LED"

iiter = 0
tperiode=3 #minuten
isautofocus=False

while True:
	if isautofocus and (iiter%10)==0:
		
		# autofocus
		api.imcontrol.setLaserActive(laserNameR, True)
		api.imcontrol.autoFocus(rangez=200, resolutionz=10)
		api.imcontrol.setLaserActive(laserNameR, False)
	# image for red
	print("Laser RED")
	api.imcontrol.setLaserActive(laserNameR, True)
	time.sleep(5)
	api.imcontrol.snapImage()
	api.imcontrol.setLaserActive(laserNameR, False)

	# image for blue
	print("Laser Blue")
	api.imcontrol.setLaserActive(laserNameB, True)
	time.sleep(5)
	api.imcontrol.snapImage()
	api.imcontrol.setLaserActive(laserNameB, False)


	time.sleep(tperiode*60)
	print(iiter)
	iiter +=1
	
