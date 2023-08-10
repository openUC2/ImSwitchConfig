import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

N_images = 10
dz = 10
axis = "Z"
Twait = 0


laserName = api.imcontrol.getLaserNames()
positioner = api.imcontrol.getPositionerNames()

laserNameR = "635 Laser"
laserNameB = "488 Laser"


iiter = 1

# timesteps 
for dt in range(10):
	
	# iterate over Z-planes
	for dz in range(-5, 5):
		api.imcontrol.movePositioner(positioner[0], axis, dz*10, True, True)
	
		# iterate over lasers 
		for dc in range(2):
			if dc==0:
				api.imcontrol.setLaserActive(laserNameR, True)
				api.imcontrol.setLaserActive(laserNameB, False)
			if dc==1:
				api.imcontrol.setLaserActive(laserNameB, True)
				api.imcontrol.setLaserActive(laserNameR, False)
	
			# iterate over pattterns and save images
			for iPattern in range(9):
				api.imcontrol.simPatternByID(iPattern)
				api.imcontrol.snapImage() 
