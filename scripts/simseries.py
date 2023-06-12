mainWindow.setCurrentModule('imcontrol')
import time
for i in range(10):
	print(i)
	time.sleep(1)
	api.imcontrol.updateDisplayImageImageFastAPISIM(i%8, "192.168.137.154", "8000")
	time.sleep(.1)
	api.imcontrol.snapImage() 