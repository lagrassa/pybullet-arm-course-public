from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot
from pybullet_arm_course.environment_setup import plot_position
from pybullet_arm_course.robot_control import inverse_kinematics, control_joints
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



"""
Step 2a. 
The next goal is to control the robot to go to a set of joint positions.  For
joint control, we specify the joint angles.  Make joint numbers [0,1,2,3,4,5,6]
of the robot go to [0, -37, 0, -170, 0, 132, 45].  For example, if we want
joints [4,5,6] of the robot to go to [0, 132, 45] we would do:
>>> control_joints(my_robot, [4,5,6], [0, 132, 45])

TODO: make joint numbers [0,1,2,3,4,5,6] go to [0, -37, 0, -170, 0, 132, 45]
"""



"""
Step 2b.
We can also change the maximum force or how "hard the robot will try" to get to
the joints. Try changing the max_force parameter for the same joint numbers and
joint angles. What happens?
>>> control_joints(my_robot, [4,5,6], [0, 132, 45], max_force=10)

TODO: try changing max_force
"""



"""
Step 2c.
Get the robot to move to the desired joint values very slowly. What values did
you use?

TODO: make the robot move its joints slowly
"""



"""
Step 2d.
Pick your own joint values. What happens when you send the robot to those
values? Which values did you choose?

TODO: control the robot to go to those desired joint values
"""
#my_desired_joints = TODO 



"""
Step 3.
The next part of this lab uses the inverse kinematics we learned about to go to
a desired pose for the gripper. To get the desired joints, call our
inverse_kinematics function like so. The inputs are position and rotation.  For
example, to get the joints required to move to the point
[[0.6, 0, 0.4], FIXED_ROTATION] we would do:
>>> desired_joints_example = inverse_kinematics(my_robot, [0.6, 0, 0.4], FIXED_ROTATION)

TODO: Find the desired joints corresponding to the position (0.5, 0.1, 0.3) and
FIXED_ROTATION.  Set those equal to a variable called desired_joints
"""
#desired_joints = TODO



"""
Step 4: Teleoperation.
We wrote a function that takes in as input a list of coordinates and outputs the
position. Call that function, and use the input as where to move the robot. 
>>> while True: 
>>>     position_string = input("Write position values separated by commas. Ex: 0.5, 0, 0.4 \n")
>>>     position = position_string_to_position(position_string)

TODO: Get the desired joints corresponding to the position input and set the
robot to go to those joint values.
"""
#while True: 
#    position_string = input("Write position values separated by commas. Ex: 0.5, 0, 0.4")
#    position = position_string_to_position(position_string)
#    plot_position(position)
