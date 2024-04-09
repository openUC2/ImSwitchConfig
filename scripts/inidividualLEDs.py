mPattern = list(({"id":1,"r":0, "g":1, "b":0},
			{"id":2, "r":0, "g":1, "b":0},
			{"id":3, "r":0, "g":1, "b":0},
			{"id":4, "r":0, "g":1, "b":0},
			{"id":5, "r":0, "g":1, "b":0}))
for i in range(20):
	api.imcontrol.setSpecial(mPattern, 255, True)