from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot
from pybullet_arm_course.environment_setup import plot_position, make_basic_scene
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints, grasp_object, place_object
from pybullet_arm_course.utils import position_string_to_position


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

"""
Step 2. 
For this lab, we will be controlling the robot to go to an object and grasp it. 
We have already implemented the last lab for you. All you need to do is select
the object for it to grasp.
>>> red_rod, green_rod, blue_rod = make_basic_scene()
>>> grasp_object(my_robot, YOUR_OBJECT_HERE)

TODO: make the robot grasp red_rod.
"""


"""
Step 3a.

Now we want the robot to place it somewhere. Input a position [x,y,z], and run
place_object(my_robot, YOUR_OBJECT_HERE) which will go to that location and open the grippers for you.
>>> place_object(my_robot, YOUR_OBJECT_HERE)

TODO: make the robot place red_rod at the position [0.4, 0.5, 0.02]
"""



"""
Step 3b.
Change the last number of the position. What happens?

TODO: change the last number of the input position. 
"""

