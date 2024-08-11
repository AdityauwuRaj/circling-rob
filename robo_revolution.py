'''
*****************************************************************************************
*
* All the functions in this file are used to control the robot in the CoppeliaSim
* simulation via APIs
*
*****************************************************************************************
'''

import sys
import traceback
import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

############################## GLOBAL VARIABLES ######################################



############################ USER DEFINED FUNCTIONS ##################################
def operate(a, b, timing):
    left_wheel = sim.getObject("/joint_l")  #this will assign to left wheel
    right_wheel = sim.getObject("/joint_r") #this will assign to right wheel
    car = sim.getObject("/crn_bot")         #this will assign to car/robot
    sim.setObjectInt32Param(right_wheel, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)   #we can direct velocity of right wheel
    sim.setObjectInt32Param(left_wheel, sim.jointintparam_dynctrlmode, sim.jointdynctrl_velocity)    #we can direct velocity of left wheel
    sim.setJointTargetVelocity(left_wheel, a)     #we can control velocity of left wheel
    sim.setJointTargetVelocity(right_wheel, b)    #we can control velocity of right wheel
    time.sleep(timing)    #time duraction for revolution
    sim.setJointTargetVelocity(left_wheel, 0)        #stops the left wheel
    sim.setJointTargetVelocity(right_wheel, 0)       #stops the rightt wheel
    
   
    
################################ MAIN FUNCTION #######################################

def simulator(sim):
    """
	Purpose:
	---
	This function should implement the control logic for the given problem statement
	You are required to actuate the rotary joints of the robot in this function, such that
	it does the required tasks.

	Input Arguments:
	---
	`sim`    :   [ object ]
		ZeroMQ RemoteAPI object

	Returns:
	---
	None

	Example call:
	---
	simulator(sim)
	"""

    #### YOUR CODE HERE ####
    
    
    operate(-8.5,12, 2)   #calling the functions 3 times
    time.sleep(1.5)
    operate(0.5, -3, 2.9)
    time.sleep(1.5)
    operate(-7, 12, 2)
  
    return None


######### YOU ARE NOT ALLOWED TO MAKE CHANGES TO THE MAIN CODE BELOW #########

if __name__ == "__main__":
    client = RemoteAPIClient()
    sim = client.getObject('sim')

    try:

        ## Start the simulation using ZeroMQ RemoteAPI
        try:
            return_code = sim.startSimulation()
            if sim.getSimulationState() != sim.simulation_stopped:
                print('\nSimulation started correctly in CoppeliaSim.')
            else:
                print('\nSimulation could not be started correctly in CoppeliaSim.')
                sys.exit()

        except Exception:
            print('\n[ERROR] Simulation could not be started !!')
            traceback.print_exc(file=sys.stdout)
            sys.exit()

        ## Runs the robot navigation logic written by participants
        try:
            simulator(sim)
            time.sleep(5)

        except Exception:
            print('\n[ERROR] Your simulator function throwed an Exception, kindly debug your code!')
            print('Stop the CoppeliaSim simulation manually if required.\n')
            traceback.print_exc(file=sys.stdout)
            print()
            sys.exit()

        ## Stop the simulation using ZeroMQ RemoteAPI
        try:
            return_code = sim.stopSimulation()
            time.sleep(0.5)
            if sim.getSimulationState() == sim.simulation_stopped:
                print('\nSimulation stopped correctly in CoppeliaSim.')
            else:
                print('\nSimulation could not be stopped correctly in CoppeliaSim.')
                sys.exit()

        except Exception:
            print('\n[ERROR] Simulation could not be stopped !!')
            traceback.print_exc(file=sys.stdout)
            sys.exit()

    except KeyboardInterrupt:
        ## Stop the simulation using ZeroMQ RemoteAPI
        return_code = sim.stopSimulation()
        time.sleep(0.5)
        if sim.getSimulationState() == sim.simulation_stopped:
            print('\nSimulation interrupted by user in CoppeliaSim.')
        else:
            print('\nSimulation could not be interrupted. Stop the simulation manually .')
            sys.exit()
