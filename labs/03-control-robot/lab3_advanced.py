import pybullet
import numpy as np
from pybullet_arm_course.robot_setup import get_gripper_position, make_robot
from pybullet_arm_course.environment_setup import get_object_position, get_object_velocity
import pybullet_arm_course.pybullet_tools.utils as pb_utils
"""
   Part 5
   The goal is to move the ball as close as possible to the target. Input your control code in the function below:

RULES: Feel free to pass in any information about the ball location,
velocity, or franka location and velocity as arguments to run_controls.
The only rule is you can only run control_joints to move the robot, no 
setting joint positions (or object positions!) directly. (otherwise this would be boring and easy)
"""

def run_controls(): #Add any arguments you want
    #TODO your code here
    print("Running control")

def setup_env(hard=False):
    robot = make_robot("/home/lagrassa/git/pybullet-arm-course/assets/franka_description/robots/franka_panda.urdf")#TODO change to location of your robot file
    sphere_radius = 0.04
    ball = pb_utils.create_sphere(sphere_radius, mass=5, color=(0.3, 0.2, 0.8, 1))
    pb_utils.enable_gravity()
    start_position = (0.5, 0, sphere_radius)
    pb_utils.set_point(ball, start_position)
    target_radius = 0.05
    height = 0.001
    target = pb_utils.create_cylinder(radius=target_radius, height=height, color=(1,0,0,1), collision=True)
    pb_utils.set_dynamics(target, lateralFriction=1, rollingFriction=1)
    if hard:
        pb_utils.set_point(target, (1.5, 0.2, height/2))
    else:
        pb_utils.set_point(target, (0.6, 0, height/2))
    pb_utils.set_real_time(False)
    return ball, target, robot

def run_test(test_length = 2000, hard=False):
    ball, target, robot = setup_env(hard=hard)
    ball_location = get_object_position(ball)
    target_location = get_object_position(target)
    gripper_position = get_gripper_position(robot)
    ball_velocity = get_object_velocity(ball)
    for t in range(test_length):
        run_controls()
        pb_utils.step_simulation()

    target_distance = np.linalg.norm(np.array(ball_location) - np.array(target_location))
    print(f"Target distance: {target_distance}")


run_test(hard=False)
