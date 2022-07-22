from pybullet_arm_course.robot_setup import make_robot
from pybullet_arm_course.environment_setup import make_basic_scene
from pybullet_arm_course.robot_control import grasp_object_for_throwing, position_for_throwing, throw
import numpy as np


RED = (1,0,0,1)
BLUE = (0,0,1,1)
GREEN = (0,1,0,1)
FIXED_ROTATION = (1, 0, 0, 0)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
OFFSETS = [-0.05, 0, 0.0]
r"""
Step 1a. This part is the same as for previous labs. Name and make your robot from a model
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

"""
Step 1b.
Here, we want to yeet rods. Therefore we need to set up the scene to have three
objects like the previous labs:
>>> red_rod, green_rod, blue_rod = make_basic_scene()

TODO: call make_basic_scene function from above
"""

"""
Step 2. 
To throw a rod, there are 3 steps you need:
1. Grasp the object
2. Get the robot arm into a throwing position
3. Throw the object

Write a for-loop that iterates over a list of the rods you've created called rod_list. Remember, 
to create a list, write a comma-separated list of your items surrounded by
square braces. For example:

>>> rod_list = [item1, item2, item3]

For each rod in the list, execute the following 3 functions:
>>> grasp_object_for_throwing(my_robot, INSERT ROD HERE, offsets=OFFSETS)
>>> position_for_throwing(my_robot)
>>> throw(my_robot, velocity=5, max_force=20)

Notice that when you execute the code above, the robot just sort of sags. How can we fix this? 
HINT: try changing velocity and/or max_force parameters.
"""

rod_list = [] # TODO: fill in rods into this list

for rod in rod_list:
    pass # TODO: delete "pass" and code the 3 steps to throw an object