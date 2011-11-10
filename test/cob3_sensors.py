#!/usr/bin/python
import openravepy
import time


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	enablesensor = 0
	
	while True:
		sensors = env.GetSensors()
		for i,sensor in enumerate(sensors):
			if (i == enablesensor):
				sensor.Configure(openravepy.Sensor.ConfigureCommand.PowerOn)
				sensor.Configure(openravepy.Sensor.ConfigureCommand.RenderDataOn)
			else:
				sensor.Configure(openravepy.Sensor.ConfigureCommand.PowerOff)
				sensor.Configure(openravepy.Sensor.ConfigureCommand.RenderDataOff)
		print "Showing sensor %s, try moving obstacles"%sensors[enablesensor].GetName()
		time.sleep(5)
		enablesensor = (enablesensor + 1) % len(sensors)
	
	env.Destroy()
