from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot
from pybullet_arm_course.environment_setup import plot_position, make_basic_scene, stamp_objects, make_basic_pushing_scene, get_object_position, CUBE_DIMS
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints, grasp_object, place_object, close_gripper
from pybullet_arm_course.utils import position_string_to_position


FIXED_ROTATION = (1, 0, 0, 0)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
r"""
Step 1. This part is the same as for all other labs. Name and make your robot from a model
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
Step 2a.
Here, the final goal is to push the objects along a goal path. First, set up the scene
to have three objects like the previous labs:
>>> red_cube, green_cube, blue_cube = make_basic_pushing_scene()
"""
# TODO: set up the scene

"""
Step 2b.
Next, define a function called goto_xyz_position that takes three arguments: x,
y, and z. This function should move the robot gripper to the position specified
in its arguments. You can use any of the functions that we've shown you so far
in previous labs.

HINT: You might find the functions inverse_kinematics and control_joints
particularly useful!
"""
def goto_xyz_position(x, y, z):
    pass

"""
Step 2c.
Modify goto_xyz_position so that it has a keyword argument called leave_stamp
(with default value False), and make it so that if this is True, then
goto_xyz_position will call stamp_objects([red_cube, green_cube, blue_cube]) as its last line.
"""

"""
Step 3a.

Push the block forward 0.2 m and leave a stamp about every 0.04 meters.
"""


"""
Step 3b.

Push the block forward 0.2 m total and leave a stamp about every 0.02 meters.
"""



