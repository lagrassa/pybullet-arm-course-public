import pybullet_arm_course.pybullet_tools.utils as pb_utils
import time
from pybullet_arm_course.pybullet_tools.ikfast.ikfast import get_ik_joints, either_inverse_kinematics
from .environment_setup import get_object_position
from .robot_setup import get_gripper_position
from collections import namedtuple
import pybullet_arm_course.pybullet_colab_tools as pct
import numpy as np
import math
import pybullet as p
import sys


FIXED_ROTATION = (1, 0, 0, 0)
MOVABLE_JOINT_NUMBERS = [0,1,2,3,4,5,6]
FRAMES = []

def reset_robot(my_robot):
    FRAMES = []
    reasonable_joint_numbers = list(range(0,7))
    reasonable_joint_positions = [0, -math.pi / 4, 0, -3 * math.pi / 4, 0, math.pi / 2, math.pi / 4]
    pb_utils.set_joint_positions(my_robot, reasonable_joint_numbers, reasonable_joint_positions)
    pb_utils.control_joint_positions(my_robot, reasonable_joint_numbers,reasonable_joint_positions, max_force=1000)


def wait_simulate_for_duration(duration, frame_every=10):
    dt = pb_utils.get_time_step()
    yaw = 80
    for i in range(int(math.ceil(duration / dt))):
        before = time.time()
        pb_utils.step_simulation()
        if FRAMES is not None and i % frame_every == 0:
            FRAMES.append(pct.make_frame(yaw))

def save_robot_control_animation(image_name=None):
    global FRAMES
    filename =  pct.make_animation(FRAMES, image_name=image_name)
    FRAMES = []
    return filename

def control_joint_positions(body, joints, positions, velocities=None, interpolate=10, frame_every = 15,time_to_run=1, verbose=False, **kwargs):
    if interpolate is not None:
        current_positions = pb_utils.get_joint_positions(body, joints)
        waypoints = np.linspace(current_positions, positions, num=interpolate)[1:]
        if verbose:
            print(f"current = {current_positions}, target = {positions}, waypoints = {waypoints}")
    else:
        waypoints = [positions]

    for pt in waypoints:
        if verbose:
            print(pt)
        pb_utils.control_joints(body, joints, pt, **kwargs)
        wait_simulate_for_duration(time_to_run / len(waypoints), frame_every=frame_every)

def control_joints(body, joints, positions, velocities=None, interpolate=10, **kwargs):
    frames = control_joint_positions(body, joints, [math.radians(p) for p in positions], velocities, interpolate=interpolate, **kwargs)

def grasp_object_for_throwing(body, object_idx, closed_pos=0.001, offsets=[0.3, 0, 0.04]):
    # closed_pos[0] -= 0.3
    grasp_object(body, object_idx, closed_pos=closed_pos, offsets=offsets)  

def back_up_to_throw(body, dx=-0.2, dy=0.0, dz=0.2):
    new_position = get_gripper_position(body)
    new_position[0] -= 0.2
    new_position[2] += 0.2
    target_joint_pos = inverse_kinematics(body, new_position, FIXED_ROTATION)
    control_joints(body, MOVABLE_JOINT_NUMBERS, target_joint_pos, max_force=20) 

def throw(my_robot, velocity, max_force, dx=0.2, dy=0, dz=0.4, closed_pos=0.000723): #0.000523 worked okay
    pb_utils.disable_real_time()
    robot_target_pos = np.array(get_gripper_position(my_robot)) + np.array([dx, dy, dz])
    target_joint_pos = inverse_kinematics(my_robot, robot_target_pos, FIXED_ROTATION)
    # import pdb; pdb.set_trace()
    #control_joints(my_robot, MOVABLE_JOINT_NUMBERS, target_joint_pos, velocities = [velocity] * 7, interpolate=2, max_force=max_force)
    control_joints(my_robot, MOVABLE_JOINT_NUMBERS + [8, 9], target_joint_pos + [closed_pos, closed_pos], velocities = [velocity] * 7, interpolate=2, max_force=max_force)

def grasp_object(body, object_idx, closed_pos = 0.015, offsets=[0, 0, 0.04]):
    open_gripper(body)
    object_position = get_object_position(object_idx)
    goal_robot_position = object_position.copy()
    goal_robot_position[2] += 0.000
    goal_robot_position[0] += offsets[0]
    goal_robot_position[1] += offsets[1]
    goal_robot_position[2] += offsets[2]
    goto_position(body, goal_robot_position)
    goal_robot_position[2] -= offsets[2]
    goto_position(body, goal_robot_position)
    close_gripper(body, closed_pos=closed_pos)

def place_object(body, position):
    buffer = 0.01
    goal_robot_position = get_gripper_position(body)
    goal_robot_position[2] += 0.05
    max_force = 60
    interpolate = 20
    goto_position(body, goal_robot_position, max_force=max_force, time_to_run=2, interpolate=interpolate)
    goal_robot_position[:1] = position[:1].copy()
    goto_position(body, goal_robot_position, max_force = max_force, time_to_run=3, interpolate=interpolate)
    goal_robot_position[2] = position[2] + buffer
    goto_position(body, goal_robot_position, max_force = max_force, time_to_run=2, interpolate=interpolate)
    open_gripper(body)

def goto_position(body, goal_robot_position, time_to_run=1, **kwargs):
    angles = inverse_kinematics(body, goal_robot_position, FIXED_ROTATION)
    control_joints(body, MOVABLE_JOINT_NUMBERS, angles, time_to_run=time_to_run, **kwargs)

def open_gripper(body, open_pos = 0.04):
    control_joint_positions(body, [8,9],[open_pos, open_pos], time_to_run=2, max_force=5*240., frame_every=30)

def close_gripper(body, closed_pos = 0.015, max_force=12):
    closed_pos = np.deg2rad(closed_pos)
    control_joint_positions(body, [8,9],[closed_pos, closed_pos], time_to_run=2, max_force=max_force, frame_every=30)

def inverse_kinematics(object_index, position, rotation):
    state = p.saveState()
    offset = 0.1
    position_up = (position[0], position[1], position[2]+offset)
    goal_ee_pose = (position_up, rotation)
    tool_link = 7
    IKFastInfo = namedtuple('IKFastInfo', ['module_name', 'base_link', 'ee_link', 'free_joints'])
    info = IKFastInfo(module_name='franka_panda.ikfast_panda_arm', base_link='panda_link0', ee_link='panda_link7',
                      free_joints=['panda_joint6'])
    ik_joints = get_ik_joints(object_index, info, tool_link)
    pb_kwargs = {"pos_tolerance": 1e-3, "ori_tolerance": 3.14*1e-3, "max_attempts": 5,
                 "max_time": 500000000, "fixed_joints": []}
    if True: #with pb_utils.LockRenderer():
        conf = next(
            either_inverse_kinematics(object_index, info, tool_link, goal_ee_pose, use_pybullet=True, **pb_kwargs),
            None)
    p.restoreState(state)
    if conf is None:
        print("**********INFEASIBLE POSITION (THINK ABOUT WHY). EXITING...************")
        sys.exit()
    return [math.degrees(a) for a in conf]

