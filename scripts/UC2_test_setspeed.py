positioner = api.imcontrol.getPositionerNames()


speed_pump = 50
speed_tomo = 5000
Nsteps = 100000

api.imcontrol.setPositionerSpeed(positioner[0], (1000,speed_pump,speed_tomo))
#xyz = focus holo, pump, rotation
api.imcontrol.movePositioner(positioner[0], "XYZ", (0,int(-speed_pump/speed_tomo*Nsteps),Nsteps))

api.imcontrol.setMotorsEnabled(positioner[0], 0)

api.imcontrol.sendTrigger(1)

api.imcontrol.post_json()

