from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot
from pybullet_arm_course.environment_setup import plot_position, make_advanced_scene
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints
from pybullet_arm_course.utils import position_string_to_position
import time


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
#TODO your make_robot code here
robot_file_location = "/home/lagrassa/git/pybullet-arm-course/assets/franka_description/robots/franka_panda.urdf"
my_robot = make_robot(robot_file_location)
bin_dims = [0.2, 0.15, 0.07]
bin_position = [0.7, 0.4, bin_dims[2]/2]
red_rod_id, green_rod_id, blue_rod_id, bin_id, = make_advanced_scene(bin_position, bin_dims)


"""
Step 2. 

We will autonomously grasp different objects and place them in the bin. 
Questions to think about:
How do we choose which position to pick from?
Are there any objects that tend to fall out of the gripper? What can we do to 
make the grasping more reliable?

Implement the following functions and call them on all the objects in the scene.
"""
def move_object_to_bin(robot_id, object_id, bin_id):
    raise NotImplementedError

def grasp_object(robot_id, object_id):
    raise NotImplementedError

def place_object(robot_id):
    raise NotImplementedError

"""
Step 3.

Implement the following functions. How do we know if an object is in the bin?
"""

def object_in_bin(object_id, bin_id):
    raise NotImplementedError

def all_objects_in_bin(object_ids, bin_id):
    raise NotImplementedError


"""
Step 4.

Time your bin picking

"""
start_time = time.time()
#TODO Your code here

assert all_objects_in_bin(object_ids, bin_id)
end_time = time.time()




