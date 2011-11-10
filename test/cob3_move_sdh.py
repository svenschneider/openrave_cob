#!/usr/bin/python
import openravepy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	jointnames = ["sdh_knuckle_joint", "sdh_finger_12_joint", "sdh_finger_13_joint", "sdh_finger_22_joint", "sdh_finger_23_joint", "sdh_thumb_2_joint", "sdh_thumb_3_joint"]
	
	home = [0.0,0.0,0.0,0.0,0.0,0.0,0.0]
	cylclosed = [0.0,0.0,1.0472,0.0,1.0472,0.0,1.0472]
	cylopen = [0.0,-0.9854,0.9472,-0.9854,0.9472,-0.9854,0.9472]
	spheropen = [1.047,-0.785,1.047,-0.785,1.047,-0.785,1.047]
	spherclosed = [1.047,-0.262,1.047,-0.262,1.047,-0.262,1.047]
	paropen = [-0.524,0,0,1.57,0.524,-0.524,0.524]
	parclosed = [1.57,0,1.57,0,0,0,0]
	point = [0,0,1.57,0,1.57,0,0]
	fist = [0,0,1.57,0,1.57,0,1.57]
	
	# use the manipulator description
	taskprob = openravepy.interfaces.TaskManipulation(robot, plannername = None)
	taskprob.ReleaseFingers()
	robot.WaitForController(0)
	taskprob.CloseFingers()
	robot.WaitForController(0)
	
	
	# setting joint values directly
	with env:
		robot.SetActiveDOFs([robot.GetJoint(name).GetDOFIndex() for name in jointnames])
		robot.SetActiveDOFValues(home)
	
	
	# manipulation planner
	manip = openravepy.interfaces.BaseManipulation(robot)
	manip.MoveActiveJoints(cylopen)
	robot.WaitForController(0)
	manip.MoveActiveJoints(cylclosed)
	robot.WaitForController(0)
	manip.MoveActiveJoints(spheropen)
	robot.WaitForController(0)
	manip.MoveActiveJoints(spherclosed)
	robot.WaitForController(0)
	#manip.MoveActiveJoints(paropen)
	#robot.WaitForController(0)
	#manip.MoveActiveJoints(parclosed)
	#robot.WaitForController(0)
	manip.MoveActiveJoints(point)
	robot.WaitForController(0)
	manip.MoveActiveJoints(fist)
	robot.WaitForController(0)
	
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()