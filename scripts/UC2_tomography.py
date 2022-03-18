import time

#mainWindow.setCurrentModule('imcontrol')

laserName = "635 Lasesr"
ledName = "White LED"

N_step_roundtrip = 53*300

#pixelsize
N_period = 20
P_period = 950 # pixels
d_reality = 25.4*1e-3/408 # dpi of huawei p20
print('pixelsize')
print(N_period*d_reality/P_period) # 1.3106295149638802e-06 m
wavelength = 488*1e-9
NA=.3
pixelsize_nyq = wavelength/NA/2 # 0.8133333333333334e-06 => undersampled



deg_per_step = 360/N_step_roundtrip
iiter = 1
positioner = api.imcontrol.getPositionerNames()


# roundtrip
delta_deg = 10
roundtrip = 360
N_steps = roundtrip//delta_deg
print(N_steps)
n_step = int(delta_deg/deg_per_step)
print(n_step)

api.imcontrol.setMotorsEnabled(positioner[0], 1)

for i in range(N_steps+1):
	api.imcontrol.movePositioner(positioner[0], "X", n_step)
	time.sleep(.2) # settle
	api.imcontrol.snapImage() 
