#!/usr/bin/python
import openravepy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	jointnames = ["head_axis_joint"]
	front = [-3.1415926]
	back = [0.0]

	
	# setting joint values directly
	with env:
		robot.SetActiveDOFs([robot.GetJoint(name).GetDOFIndex() for name in jointnames])
		robot.SetActiveDOFValues(front)
	
	manip = openravepy.interfaces.BaseManipulation(robot)
	manip.MoveActiveJoints(back)
	robot.WaitForController(0)
	manip.MoveActiveJoints(front)
	robot.WaitForController(0)
	
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()