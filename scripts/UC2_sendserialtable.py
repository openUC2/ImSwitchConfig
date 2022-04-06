mainWindow.setCurrentModule('imcontrol')
api.imcontrol.startRecording()
task = """{"task": "/motor_act", "speed0":0, "speed1":0,"speed2":40,"speed3":9000, "isforever":1, "isaccel":1} 
  {"task": "/state_set", "isdebug":0}
  {"task": "/state_act", "delay": 100}
  {
  "task": "multitable",
  "task_n": 2,
  "repeats_n": 200,
  "0": {"task": "/digital_act", "digitalid": 1, "digitalval":-1},
  "1": {"task": "/state_act", "delay": 50}
  }
  {"task": "/motor_act", "isstop":1}
  {"task": "/motor_act", "isenable":0}
  {"task": "/state_set", "isdebug":1}"""
message=api.imcontrol.send_serial(task)
#api.imcontrol.stopRecording()