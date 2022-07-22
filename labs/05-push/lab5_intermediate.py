from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot, get_gripper_position
from pybullet_arm_course.environment_setup import plot_position, make_basic_scene, make_basic_pushing_scene, get_object_position, stamp_objects
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints, open_gripper, close_gripper
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
robot_file_location = "/Users/tiffoyu/Documents/pybullet-arm-course/assets/franka_description/robots/franka_panda.urdf"
my_robot = make_robot(robot_file_location)
red_cube, green_cube, blue_cube = make_basic_pushing_scene(clear_workspace=True)

"""
Step 2a. 
Copy your function from lab5_beginner in this file.
 Using goto_position_xyz, make patterns using for loops:
 Leave an image of the cube using stamp_objects([red_cube])
"""

def make_square(side_length):
    raise NotImplementedError

"""
Step 2b.
Make a triangle with the red cube, you may need to move in both the x and y location. Try to use no more than 3 loops 
"""

def make_triangle(side_length):
    raise NotImplementedError

"""
Step 3.
Use loops to make your own pattern. Can you make a spiral?
"""

def make_shape():
    raise NotImplementedError




