from pybullet_arm_course.environment_setup import *
    
if __name__=="__main__":
    # initialize variables
    initialize_environment()
    box_pos = [0, 5, 0]
    cylinder_pos = [-2, 2, 0]
    capsule_pos = [-2, -2, 1]
    sphere_pos = [5, 0, 1]

    base_pos = [2, 2, 0]
    base_r = 1.0
    base_h = 0.2

    leg_pos = [2, 2, 1.2]
    leg_r = 0.2
    leg_h = 2

    top_pos = [2, 2, 2.3]
    top_r = 3.0
    top_h = 0.2

    width = 1
    length = 1
    height = 5
    radius = 0.5
    box_color = RED
    cylinder_color = TRANSPARENT_PURPLE

    '''
    TASK 1: Creating a scene

    First, run this file. Notice that a white box is initialized and launches itself in random directions
    at random time intervals. We want to contain its energy! Use your creativity to build a scene around 
    this randomly launching cube. 
    
    Use the create_pybullet functions (each of which is demonstrated below: box, cylinder, sphere, or 
    capsule) in order to build your scene. Note that you can stack objects on top of each other to 
    create more complex objects (see the table example below)

    NOTES: 
    - You may need to zoom out in order to see all the objects.
    - If the object falls off the plane, you will need to close out and restart the environment.
    - Sometimes, the cube takes a while to launch. Rerunning the file sometimes helps if it is taking too long.
    '''

    create_pybullet_box(pos=box_pos, width=width, length=length, height=height, color=RED)
    create_pybullet_sphere(pos=sphere_pos, radius=radius, color=GREEN)
    create_pybullet_capsule(pos=capsule_pos, radius=radius, height=height, color=YELLOW)

    # creates a table
    create_pybullet_cylinder(pos=base_pos, radius=base_r, height=base_h, color=BLUE)
    create_pybullet_cylinder(pos=leg_pos, radius=leg_r, height=leg_h, color=BLUE)
    create_pybullet_cylinder(pos=top_pos, radius=top_r, height=top_h, color=BLUE)

    # launch object around
    launch_object()