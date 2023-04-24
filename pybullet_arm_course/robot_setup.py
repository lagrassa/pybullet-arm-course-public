import pybullet_arm_course.pybullet_tools.utils as pb_utils
import pybullet_arm_course.pybullet_colab_tools as pct
import math
import numpy as np
import pybullet

def make_robot(robot_filename):
    pb_utils.connect(use_gui=False)
    for obj in pb_utils.get_bodies():
        if pb_utils.get_body_name(obj) =="panda":
            print("Robot already created")
            return 
    pct.setup_pybullet_colab()
    pb_utils.add_data_path()
    #pb_utils.load_pybullet("assets/short_floor.urdf")
    # pb_utils.set_real_time(True)
    box_geom = pb_utils.get_box_geometry(4.4, 4.4, 0.03)
    #pb_utils.create_visual_shape(box_geom, color=(1,0,1,0.5), specular=1)
    pb_utils.create_box(1,1,0.0001, mass=0, color=(0.8,0.9,1.0,1))
    pybullet.setTimeStep(1/500, physicsClientId=pb_utils.CLIENT)
    pybullet.setPhysicsEngineParameter(solverResidualThreshold=0, physicsClientId=pb_utils.CLIENT)
    with pb_utils.LockRenderer():
        robot_idx = pb_utils.load_pybullet(robot_filename, fixed_base=True)
    pb_utils.set_camera(80, -30, 2) #reasonable view for most things
    set_robot_to_reasonable_position(robot_idx)
    #pb_utils.set_dynamics(robot_idx, 9, linearDamping=0, angularDamping=0, lateralFriction=1)
    pb_utils.set_dynamics(robot_idx, 8, linearDamping=0, lateralFriction=1)
    pb_utils.set_dynamics(robot_idx, 9, linearDamping=0,lateralFriction=1)
    return robot_idx

def color_robot(robot, color):
    for part in pb_utils.get_all_links(robot):
        color_robot_part(robot, part, color)

def color_robot_part(robot, part, color):
    pb_utils.set_color(robot, link=part, color=color)

def get_gripper_position(robot):
    tool_link = 7
    return list(pb_utils.get_link_pose(robot, tool_link)[0])

def get_joint_positions(body, joints):
    return [np.rad2deg(rad) for rad in pb_utils.get_joint_positions(body, joints)]

def wait_for_robot():
    while(1):
        _ = pybullet.getKeyboardEvents()

def set_robot_to_reasonable_position(my_robot):
    reasonable_joint_numbers = list(range(0,7))
    reasonable_joint_positions = [0, -math.pi / 4, 0, -3 * math.pi / 4, 0, math.pi / 2, math.pi / 4]
    pb_utils.set_joint_positions(my_robot, reasonable_joint_numbers, reasonable_joint_positions)
