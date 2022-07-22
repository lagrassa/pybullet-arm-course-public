from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, get_gripper_position, set_robot_to_reasonable_position
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints
from pybullet_arm_course.utils import position_string_to_position, wait_and_get_pressed_key
import pybullet


FIXED_ROTATION = (0, 0, 0, 1)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
'''
Step 1a. Copy your code to make your robot here. You will need to define your 
robot filepath and call the function make_robot again:
>>> robot_file_location = ???
>>> my_robot = make_robot(robot_file_location)

For the intermediate lab, it will help to have your robot in a different 
starting position than the previous lab. Uncomment the following function and 
paste after your robot definition again:

>>> set_robot_to_reasonable_position(my_robot)

TODO: MAKE ROBOT AND set robot_file_location HERE. Give it a different name from
my_robot, then call the function set_robot_to_reasonable_position on your new 
robot name.
'''



'''
Step 1b. Here, you will teleoperate the robot. We put in some of the structure, 
but you need to fill in the blanks. You may need the following utility functions:

- get_gripper_position: returns a list of 3 numbers
- inverse_kinematics: see lab5_intermediate.py
- control joints: see lab5_intermediate.py
'''

#   Part 4a. Copy your code to make your robot here
#   Part 4b: 
#   Here, you will teleoperate the robot. We put in some of the structure, but you need to fill in the blanks.
#   You may need the utility function get_gripper_position which returns a list of 3 numbers that is the position 
#   
amount_to_move = 0.05 #5cm
FIXED_ROTATION = (1,0,0,0)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
while True:
    key_pressed = wait_and_get_pressed_key()
    if key_pressed == "w":
        print("Moving backward")
        #TODO move robot 5cm backward (in the negative x direction)
    if key_pressed == "s":
        print("Moving forward")
        #TODO move robot 5cm forward (in the positive x direction)
    if key_pressed == "d":
        print("Moving robot to the right")
        #TODO move robot 5cm to the right (positive y direction)
    if key_pressed == "a":
        print("Moving robot to the left")
        #TODO move robot 5cm to the left (negative y direction)
    if key_pressed == "u":
        print("Moving robot up")
        #TODO move robot 5cm up (positive z direction)
    if key_pressed == "j":
        print("Moving robot down")
        #TODO move robot 5cm down (negative z direction)

