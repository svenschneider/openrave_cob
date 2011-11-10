#!/usr/bin/python
import openravepy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	print "Robot", robot.GetName(), "has", robot.GetDOF(), "joints"
	print "Joints:\n", robot.GetJoints()
	print "Links:\n", robot.GetLinks()
	print "Joint limits:\n", robot.GetDOFLimits()
	print "Joints values:\n", robot.GetDOFValues()
	print "Manipulators:", robot.GetManipulators() 
	print "Active manipulator:", robot.GetActiveManipulator()
	print "Controller: ", robot.GetController()
	
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()