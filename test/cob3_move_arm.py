#!/usr/bin/python
import openravepy
import numpy


if __name__ == "__main__":
	env = openravepy.Environment() 
	env.SetViewer("qtcoin") 
	env.Load("../cob_default_config/envs/cob3-1.env.xml")
	robot = env.GetRobot("cob3-1")
	
	ikmodel = openravepy.databases.inversekinematics.InverseKinematicsModel(robot, iktype = openravepy.IkParameterization.Type.Transform6D)
	if not ikmodel.load():
		print "Generating IK for arm"
		ikmodel.autogenerate()
	
	jointnames = ["arm_1_joint", "arm_2_joint", "arm_3_joint", "arm_4_joint", "arm_5_joint", "arm_6_joint", "arm_7_joint"]
	
	# back side positions
	home = [0, 0, 0, 0, 0, 0, 0]
	folded = [-1.1572567240035734, -1.9104664691761568, -2.5334780195730255, -1.7853311980377056, -0.072798739390243047, 0.91767934923272776, -1.8876618005378798]
	pregrasp = [-1.3813422735995828, -1.9312548399287899, -1.7251153715474463, -1.4565057632094409, 0.7169946808744756, 1.0560171841958719, -2.1230019199424044]
	pre_look_at_table = [-1.4117332144741783, -1.0933802021501384, -2.8143842535448362, -2.0943951023931953, 0.32534573315130511, 1.5282712545442345, 1.7578776443176236]
	look_at_table = [-1.90413007129692, -0.53676863707511047, -2.9670597283903604, -1.2371477849958294, 0.078324145463379971, 1.1674038268438356, 1.7663080901665025]
	
	# front side positions
	overtray = [2.9670597283903604, -1.0850245914937158, -2.8517849530558705, -1.490963271231841, 0.69903542231877758, 1.0647794507576016, -1.9565543563358203]
	tray = [2.8545925371816212, -1.1411602564796222, -2.879793265790644, -1.4768269321056455, 0.55049237134044171, 1.0657754724693511, -2.029771517204098]
	intermediateback = [-0.92723326226047276, -1.0878091156907497, -1.7511329390916868, -2.0350967789643617, 0.75547017562671237, 1.55547223138452, -2.6139619402066767]
	intermediatefront = [2.567286997401903, -0.76650447903842134, -2.879793265790644, -1.3169067774275871, 0.59769801545593759, 1.3751587638740583, -1.9299075952888678]
	
	
	# setting joint values directly
	with env:
		robot.SetActiveDOFs([robot.GetJoint(name).GetDOFIndex() for name in jointnames])
		robot.SetActiveDOFValues(folded)
	
	# arm planner
	armmanip = openravepy.interfaces.BaseManipulation(robot)
	
	# move to cartesian pose
	goal = numpy.array([[0, 0, -1, -0.7], [0, 1, 0, 0], [1, 0, 0, 0.842], [0, 0, 0, 1]])
	armmanip.MoveToHandPosition(matrices = [goal], seedik = 16)
	robot.WaitForController(0)
	
	# plan and move to configuration
	armmanip.MoveManipulator(look_at_table)
	robot.WaitForController(0)
	armmanip.MoveManipulator(pre_look_at_table)
	robot.WaitForController(0)
	armmanip.MoveManipulator(folded)
	robot.WaitForController(0)
	armmanip.MoveManipulator(pregrasp)
	robot.WaitForController(0)
	armmanip.MoveManipulator(intermediateback)
	robot.WaitForController(0)
	armmanip.MoveManipulator(intermediatefront)
	robot.WaitForController(0)
	
	print "Press enter to exit"
	raw_input()
	
	env.Destroy()