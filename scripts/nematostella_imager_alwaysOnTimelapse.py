import numpy as np
import time

mainWindow.setCurrentModule('imcontrol')

intensityAll = 20
#api.imcontrol.LsetAll(1,(intensityAll,intensityAll,intensityAll)) # RGB 

iiter = 0
tperiode=20 #minuten
isautofocus=False


while True:
	print(iiter)
	api.imcontrol.snapImage()
	time.sleep(tperiode)
	iiter +=1
	
