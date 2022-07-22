import pybullet_arm_course.pybullet_tools.utils as pb_utils
import math
import pybullet

def make_robot(robot_filename):
    pb_utils.connect(use_gui=True)
    pb_utils.add_data_path()
    pb_utils.load_pybullet("plane.urdf")
    # pb_utils.set_real_time(True)
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

def wait_for_robot():
    while(1):
        _ = pybullet.getKeyboardEvents()

def set_robot_to_reasonable_position(my_robot):
    reasonable_joint_numbers = list(range(0,7))
    reasonable_joint_positions = [0, -math.pi / 4, 0, -3 * math.pi / 4, 0, math.pi / 2, math.pi / 4]
    pb_utils.set_joint_positions(my_robot, reasonable_joint_numbers, reasonable_joint_positions)
