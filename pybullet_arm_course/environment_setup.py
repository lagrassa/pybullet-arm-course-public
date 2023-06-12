import pybullet
import time
import random
import os
import numpy as np
import pybullet_data
import pybullet_arm_course.pybullet_tools.utils as pb_utils

RED = [1., 0., 0., 1.]
GREEN = [0., 1., 0., 1.]
BLUE = [0., 0., 1., 1.]
YELLOW = [1., 1., 0., 1.]
TRANSPARENT_PURPLE = [1., 0., 1., 0.5]
BOX_DIMS = [0.12, 0.03, 0.03]
CUBE_DIMS = [0.03, 0.03, 0.03]
BOX_COLORS = [(1,0,0,1), (0,1,0,1), (0,0,1,1)]

SMALL = 0.1
MEDIUM = 0.5
BIG = 1.

DUCK = "duck"
CUBE = "cube"
WEIGHT = "weight"
BEAR = "bear"

object_dict = {
    "duck": ("duck.obj", "duck_vhacd.obj"),
    "cube": ("cube.obj", "cube.obj"),
    "weight": ("stone.obj", "stone.obj"),
    "bear":("teddy2_VHACD_CHs.obj", "teddy2_VHACD_CHs.obj")
}

def initialize_object(object, size=SMALL):
    try:
        object_tuple = object_dict[object]
    except:
        raise ValueError("""You inputted an invalid object. Make sure you specify a case-sensitive object 
                            from the following list: DUCK, CUBE, WEIGHT, BEAR""")

    pybullet.connect(pybullet.GUI)

    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    pybullet.loadURDF("plane_transparent.urdf", useMaximalCoordinates=True)
    #disable rendering during creation.
    pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI, 0)

    shift1 = [0, 0.0, 0]
    shift2 = [0, 0, 0]

    meshScale = [size, size, size]

    # initialize a duck
    visualShapeId = pybullet.createVisualShape(shapeType=pybullet.GEOM_MESH,
                                               fileName=object_tuple[0],
                                               meshScale=meshScale)
    collisionShapeId = pybullet.createCollisionShape(shapeType=pybullet.GEOM_MESH,
                                                     fileName=object_tuple[1],
                                                     meshScale=meshScale)

    assert(visualShapeId == collisionShapeId == 0)

    mb = pybullet.createMultiBody(baseMass=1,
                                  baseInertialFramePosition=[0, 0, 0],
                                  baseCollisionShapeIndex=collisionShapeId,
                                  baseVisualShapeIndex=visualShapeId,
                                  useMaximalCoordinates=False)

    pybullet.changeVisualShape(mb, -1, rgbaColor=[1, 1, 1, 1])
    pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_RENDERING, 1)
    pybullet.setGravity(0, 0, -10)
    pybullet.setRealTimeSimulation(1)
    return mb

def change_to_colors(colors):
    current_color = 0
    while (1):
        keys = pybullet.getKeyboardEvents()
        if keys and len(colors) > 0:
            key = list(keys.keys())[0]
            if keys[key] == pybullet.KEY_WAS_RELEASED:
                current_color = (current_color + 1) % len(colors)
                pybullet.changeVisualShape(1, -1, rgbaColor=colors[current_color])
                # adapted from pybullet demo: create_visual_shape_array.py

def initialize_environment():
    pybullet.connect(pybullet.GUI)
    pybullet.setAdditionalSearchPath(pybullet_data.getDataPath())
    pybullet.loadURDF("plane_transparent.urdf", useMaximalCoordinates=True)
    #disable rendering during creation.
    pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_GUI, 0)
    pybullet.configureDebugVisualizer(pybullet.COV_ENABLE_RENDERING, 1)
    pybullet.setGravity(0, 0, -10)
    pybullet.setRealTimeSimulation(1)

def spawn_object(obj, size, color):
    try:
        object_tuple = object_dict[obj]
    except:
        raise ValueError("""You inputted an invalid object. Make sure you specify a case-sensitive object 
                            from the following list: DUCK, CUBE, WEIGHT, BEAR""")

    meshScale = [size, size, size]

    # initialize a duck
    visual_id = pybullet.createVisualShape(shapeType=pybullet.GEOM_MESH,
                                            fileName=object_tuple[0],
                                            meshScale=meshScale)
    collision_id = pybullet.createCollisionShape(shapeType=pybullet.GEOM_MESH,
                                                fileName=object_tuple[1],
                                                meshScale=meshScale)

    multibody_id = pybullet.createMultiBody(baseMass=1,
                            baseInertialFramePosition=[0, 0, 0],
                            baseCollisionShapeIndex=collision_id,
                            baseVisualShapeIndex=visual_id,
                            useMaximalCoordinates=False)
    
    pybullet.changeVisualShape(multibody_id, -1, rgbaColor=color)
    return multibody_id, collision_id, visual_id

def any_key_is_pressed():
    keys = pybullet.getKeyboardEvents()
    return any(state & pybullet.KEY_WAS_RELEASED for state in keys.values())

def make_basic_scene(dims=None):
    pb_utils.enable_gravity()
    #pybullet.setTimeStep(1/500.,physicsClientId=pb_utils.CLIENT)
    #delete any other objects in scene:
    for obj in pb_utils.get_bodies():
        if pb_utils.get_body_name(obj) not in ["plane", "panda"]:
            print("Removing body from scene")
            pb_utils.remove_body(obj)
    mass = 0.1
    if dims is None:
        dims = BOX_DIMS
    points = [(0.27, 0.1, dims[2]/2), (0.5, -0.07, dims[2]/2), (0.4, 0.2, dims[2]/2)]
    boxes = []
    for color, point in zip(BOX_COLORS, points):
        boxes.append(pb_utils.create_box(dims[0], dims[1], dims[2], color=color, mass=mass))
        pb_utils.set_point(boxes[-1], point)
        #pb_utils.set_dynamics(boxes[-1], rollingFriction=0.2, lateralFriction=0.9)
        pb_utils.set_dynamics(boxes[-1], rollingFriction=0.00001, spinningFriction=0.8, lateralFriction=1)
    return boxes

def make_basic_pushing_scene(clear_workspace=False):
    boxes = make_basic_scene(CUBE_DIMS)
    z_val = CUBE_DIMS[2]/2
    if clear_workspace:
        pb_utils.set_point(boxes[1], (0.5, 0.8, z_val))
        pb_utils.set_point(boxes[2], (0.5, -0.8, z_val))
    return boxes

def stamp_objects(boxes):
    #assumes objects are boxes
    for box, color in zip(boxes, BOX_COLORS):
        current_pose = pb_utils.get_pose(box)
        color_transparent = color[:3]+(0.2,)
        transparent_box = pb_utils.create_box(CUBE_DIMS[0], CUBE_DIMS[1], CUBE_DIMS[2], color = color_transparent, collision=False)
        pb_utils.set_pose(transparent_box, current_pose)



def make_advanced_scene(bin_position, bin_dims, bin_thickness=0.005):
    boxes = make_basic_scene()
    bin_color = (1,1,0,0.7)
    bottom_bin = pb_utils.create_box(bin_dims[0],bin_dims[1], bin_thickness, color=bin_color)
    plus_y_bin = pb_utils.create_box(bin_dims[0], bin_thickness, bin_dims[2], color=bin_color)
    minus_y_bin = pb_utils.create_box(bin_dims[0], bin_thickness, bin_dims[2], color=bin_color)
    plus_x_bin = pb_utils.create_box(bin_thickness, bin_dims[1]-2*bin_thickness, bin_dims[2], color=bin_color)
    minus_x_bin = pb_utils.create_box(bin_thickness, bin_dims[1]-2*bin_thickness, bin_dims[2], color=bin_color)
    bottom_position = bin_position.copy()
    bottom_position[2] = bin_thickness/2.
    plus_y_position = bin_position.copy()
    plus_y_position[2] = bin_dims[2]/2
    plus_y_position[1] += bin_dims[1]/2
    minus_y_position = plus_y_position.copy()
    minus_y_position[1] -= bin_dims[1]
    plus_x_position = bin_position.copy()
    plus_x_position[2] = bin_dims[2]/2
    plus_x_position[0] += bin_dims[0]/2 + bin_thickness/2
    minus_x_position = plus_x_position.copy()
    minus_x_position[0] -= bin_dims[0] + bin_thickness
    pb_utils.set_point(bottom_bin,bottom_position)
    pb_utils.set_point(plus_y_bin,plus_y_position)
    pb_utils.set_point(minus_y_bin,minus_y_position)
    pb_utils.set_point(plus_x_bin,plus_x_position)
    pb_utils.set_point(minus_x_bin,minus_x_position)
    input("OK?")
    return [bottom_bin,] + boxes


def uniform_size():
    return BIG

def uniform_object():
    return CUBE

def uniform_color():
    return [1, 1, 1, 1]

def make_objects_of_size_and_color(size_func=uniform_size, object_func=uniform_object, color_func=uniform_color):
    current_color = 0
    while (1):
        if any_key_is_pressed():
            spawn_object(object_func, size_func, color_func)

def set_position(body_id, pos):
    pb_utils.set_point(body_id, pb_utils.Point(pos[0], pos[1], pos[2]))

def create_pybullet_box(pos=[0, 0, 0], width=1, length=1, height=1, color=[1., 1., 1., 1.]):
    # creates target box st. launch_box will launch a box at the target box
    pb_utils.create_box(width, length, height, color=color)
    box_geometry = pb_utils.get_box_geometry(width, length, height)
    collision_id, visual_id = pb_utils.create_shape(geometry=box_geometry)
    body_id = pb_utils.create_body(collision_id, visual_id)
    pb_utils.set_point(body_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(visual_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(collision_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_color(body_id, color)
    pb_utils.set_color(collision_id, color)
    pb_utils.set_color(visual_id, color)
    return body_id

def create_pybullet_cylinder(pos=[0, 0, 0], radius=1, height=1, color=[1., 1., 1., 1.]):
    pb_utils.create_cylinder(radius, height, color=color)
    cylinder_geometry = pb_utils.get_cylinder_geometry(radius, height)
    collision_id, visual_id = pb_utils.create_shape(geometry=cylinder_geometry)
    body_id = pb_utils.create_body(collision_id, visual_id)
    pb_utils.set_point(body_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(visual_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(collision_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_color(body_id, color)
    pb_utils.set_color(collision_id, color)
    pb_utils.set_color(visual_id, color)
    return body_id

def create_pybullet_capsule(pos=[0, 0, 0], radius=1, height=1, color=[1., 1., 1., 1.]):
    pb_utils.create_capsule(radius, height, color=color)
    capsule_geometry = pb_utils.get_capsule_geometry(radius, height)
    collision_id, visual_id = pb_utils.create_shape(geometry=capsule_geometry)
    body_id = pb_utils.create_body(collision_id, visual_id)
    pb_utils.set_point(body_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(visual_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(collision_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_color(body_id, color)
    pb_utils.set_color(collision_id, color)
    pb_utils.set_color(visual_id, color)
    return body_id

def create_pybullet_sphere(pos=[0, 0, 0], radius=1, color=[1., 1., 1., 1.]):
    pb_utils.create_sphere(radius, color=color)
    sphere_geometry = pb_utils.get_sphere_geometry(radius)
    collision_id, visual_id = pb_utils.create_shape(geometry=sphere_geometry)
    body_id = pb_utils.create_body(collision_id, visual_id)
    pb_utils.set_point(body_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(visual_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_point(collision_id, pb_utils.Point(pos[0], pos[1], pos[2]))
    pb_utils.set_color(body_id, color)
    pb_utils.set_color(collision_id, color)
    pb_utils.set_color(visual_id, color)
    return body_id


def launch_object():
    DURATION = 10000
    ALPHA = 100000
    # THIS MOVES, BUT NOT WELL
    box_id, _, _ = spawn_object(uniform_object(), uniform_size(), uniform_color())
    cubeStartPos = [0, 0, 1]
    cubeStartOrientation = pybullet.getQuaternionFromEuler([0, 0, 0])

    for i in range(DURATION):
        pybullet.stepSimulation()
        time.sleep(1./240.)
        box_pos, _ = pb_utils.get_pose(box_id)
        target_pos = np.random.rand(3) - 0.5
        box_pos = np.array(box_pos)

        force = ALPHA * target_pos
        # to ensure the force is only applied in the xy direction
        force[2] = 0
        pybullet.applyExternalForce(objectUniqueId=box_id, linkIndex=-1, forceObj=force, posObj=box_pos, flags=pybullet.WORLD_FRAME)
    print("Simulation ended normally.")
    pybullet.disconnect()

def set_gravity_z_axis(gravitational_constant):
    pybullet.setGravity(0,0,gravitational_constant)

def set_gravity_all_axes(gravity_for_each_axis):
    pybullet.setGravity(*gravity_for_each_axis)

def set_simulation_time_step(time_step):
    pybullet.setTimeStep(time_step)

def simulation_is_running():
    return pybullet.isConnected()

def get_object_position(object_index):
    return list(pb_utils.get_link_pose(object_index, -1)[0])

def get_object_velocity(object_index):
    return list(pb_utils.get_velocity(object_index)[0])

def plot_position(position):
    sphere = pb_utils.create_sphere(radius=0.01, collision=False)
    pb_utils.set_point(sphere, position)

