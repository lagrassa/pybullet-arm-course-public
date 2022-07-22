from pybullet_arm_course.robot_setup import make_robot, color_robot, color_robot_part, wait_for_robot

RED = (1,0,0,1)
BLUE = (0,0,1,1)
GREEN = (0,1,0,1)
'''
Step 1, name and make your robot from a model file. Ex.. 
The input to this function is the name of the robot model. The file name is
franka_panda.urdf.
'''
# Input the location of this file, using slashes for directories forward on mac and backward on windows. For example, 
robot_file_location = r"/Users/tiffoyu/Documents/pybullet-arm-course/assets/franka_description/robots/franka_panda.urdf"

#   Windows uses backslashes, so it might look like
#robot_file_location = r"C:\Users\jessie\Documents\pybullet_arm_course\assets\franka_description\robots\franka_panda.urdf"
#   Example creating the robot:
my_robot = make_robot(robot_file_location)





#   TODO MAKE ROBOT AND set robot_file_location HERE


#   Step 2, color your robot. Ex.
#   The first input is the robot. The second input is the color. 
#   Example:
#color_robot(my_robot, RED)
#   TODO color the robot blue

#   Step 3. Color parts of the robot. The second input to the function is the 
#   part number
#   Example: To color the 4th part of the robot, write:
#color_robot_part(my_robot, 1,BLUE)
#   TODO color the 2nd part of the robot red. 
#   As a challenge, alternate between different parts of the robot yellow and red
#
wait_for_robot()
#   An error might occur. This is expected! Write down the error in your lab notebook and what you think triggered it. 
