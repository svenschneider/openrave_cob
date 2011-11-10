#!/usr/bin/python
import openravepy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	basemanip = openravepy.interfaces.BaseManipulation(robot, plannername = None)
	with env:
		robot.SetActiveDOFs([], openravepy.Robot.DOFAffine.X | openravepy.Robot.DOFAffine.Y | openravepy.Robot.DOFAffine.RotationAxis, [0, 0, 1])
		basemanip.MoveActiveJoints(goal = [2.8, -1.3, 0], maxiter = 5000, steplength = 0.15, maxtries = 2)
	robot.WaitForController(0)
    
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()