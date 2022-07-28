import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')


lensName1 = "Lens 1"
lensName2 = "Lens 2"



for lensPos in range(0,100):
	
	api.imcontrol.setLaserValue(lensName1, lensPos)
	api.imcontrol.setLaserActive(lensName1, True)
	api.imcontrol.setLaserValue(lensName2, lensPos)
	api.imcontrol.setLaserActive(lensName2, True)
	time.sleep(.1)
		
	api.imcontrol.snapImage(name="OCT_image_lensPos_"+str(lensPos)) 
	

