from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot, get_gripper_position
from pybullet_arm_course.environment_setup import plot_position, make_basic_scene, get_object_position
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints, open_gripper, close_gripper
from pybullet_arm_course.utils import position_string_to_position


RED = (1,0,0,1)
BLUE = (0,0,1,1)
GREEN = (0,1,0,1)
FIXED_ROTATION = (1, 0, 0, 0)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
r"""
Step 1. This part is the same as for lab 2. Name and make your robot from a model
file. The file name is franka_panda.urdf. First, input the location of this
file, using slashes for directories forward on mac and backward on windows.  For
example, 
>>> robot_file_location = r"/Users/lagrassa/Documents/pybullet_arm_course/assets/franka_description/robots/franka_panda.urdf"

Windows uses backslashes, so it might look like
>>> robot_file_location = r"C:\Users\jessie\projects\pybullet-arm-course\assets\franka_description\robots\franka_panda.urdf"

Next, make the robot. The input to this function is the name of the robot model.
For example,
>>> my_robot = make_robot(robot_file_location)

TODO: MAKE ROBOT AND set robot_file_location HERE. Give it a different name from
my_robot
"""
robot_file_location = "/Users/tiffoyu/Documents/pybullet-arm-course/assets/franka_description/robots/franka_panda.urdf"
my_robot = make_robot(robot_file_location)
red_rod, green_rod, blue_rod = make_basic_scene()
open_gripper(my_robot)

"""
Step 2. 
Instead of calling our functions to grasp and object, you will do it! Below we 
gave examples of useful functions.
>>> red_rod_position = get_object_position(red_rod)
>>> open_gripper(my_robot)
>>> close_gripper(my_robot)
>>> close_gripper(my_robot, closed_width=width) #useful if you want to adjust the width

Make the robot
1.  Go to a location 0.04 m above the red rod
2.  Open its gripper
3.  Go down 0.04 m 
4.  Close its gripper

You may need to toggle the max_force parameter to close_gripper, and control_joints
Other distances besides 0.04 m will work

To do this sort of thing, you can get the object location with 
>>> red_rod_position = get_object_position(red_rod)

And then modify it to go where you want
>>> goal_location = red_rod_position
>>> goal_location[2] = goal_location[2] + 0.04 #goes 0.04 m above the red rod
>>> goal_joint_positions = inverse_kinematics(my_robot, goal_location, FIXED_ROTATION)
>>> control_joints(my_robot, MOVABLE_JOINT_NUMBERS, goal_joint_positions)

"""






"""
Step 3.

Last we will implement place. 
Make the robot place the object at a location you choose by

1. Going to a location 0.02 m above the goal location using inverse_kinematics and control_joints
2. Open its gripper

You may need to toggle the max_force parameter to open_gripper, close_gripper, and control_joints

"""


