#!/usr/bin/python
import openravepy
import numpy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	jointnames = ["torso_lower_neck_pan_joint", "torso_lower_neck_tilt_joint", "torso_upper_neck_pan_joint", "torso_upper_neck_tilt_joint"]
	home = [0.0,0.0,0.0,0.0]
	left = [-0.025,0.0,-0.05,0.0]
	right = [0.025,0.0,0.05,0.0]
	front = [0,0.1,0,0.15]
	back = [0,-0.1,0,-0.15]

	
	# setting joint values directly
	with env:
		robot.SetActiveDOFs([robot.GetJoint(name).GetDOFIndex() for name in jointnames])
		robot.SetActiveDOFValues(front)
	
	manip = openravepy.interfaces.BaseManipulation(robot)
	manip.MoveActiveJoints(back)
	robot.WaitForController(0)
	manip.MoveActiveJoints(front)
	robot.WaitForController(0)
	manip.MoveActiveJoints(left)
	robot.WaitForController(0)
	manip.MoveActiveJoints(right)
	robot.WaitForController(0)
	manip.MoveActiveJoints(home)
	robot.WaitForController(0)
	
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()