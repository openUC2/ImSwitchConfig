import numpy as np
import time

positionerName = api.imcontrol.getPositionerNames()[0]
api.imcontrol.movePositioner(positionerName, "X", 10000, False, False)
time.sleep(0.05)
t0 = time.time()
for _ in range (10):
	print(api.imcontrol.getPositionerPositions(1))
	print(time.time()-t0)
	t0 = time.time()
