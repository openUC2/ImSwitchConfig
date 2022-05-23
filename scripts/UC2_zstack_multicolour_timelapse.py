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




while True:
	laser = api.imcontrol.setLaserActive(laserNameR, True)
	time.sleep(5)
	
	# take zstack
	#api.imcontrol.setLaserActive(laserName, True)
	api.imcontrol.movePositioner(positioner[0], axis, -N_images*dz/2)
	time.sleep(5)
	for i_pos in range(N_images):
		api.imcontrol.movePositioner(positioner[0], axis, dz)
		time.sleep(1)
		api.imcontrol.snapImage() 
		
	api.imcontrol.movePositioner(positioner[0], axis, -N_images*dz/2)

	
	
	laser = api.imcontrol.setLaserActive(laserNameR, False)
	time.sleep(1)
	api.imcontrol.setLaserActive(laserNameB, True)
	time.sleep(5)
	
	
	# take zstack
	#api.imcontrol.setLaserActive(laserName, True)
	api.imcontrol.movePositioner(positioner[0], axis, -N_images*dz/2)
	time.sleep(5)

	for i_pos in range(N_images):
		api.imcontrol.movePositioner(positioner[0], axis, dz)
		time.sleep(1)
		api.imcontrol.snapImage() 
		
	api.imcontrol.movePositioner(positioner[0], axis, -N_images*dz/2)

	api.imcontrol.setLaserActive(laserNameB, False)
		
	time.sleep(Twait*60)
	print(iiter)
	iiter +=1
	

