from pybullet_arm_course.environment_setup import *
from pybullet_planning import set_point

RED = [1., 0., 0., 1.]
GREEN = [0., 1., 0., 1.]
BLUE = [0., 0., 1., 1.]
YELLOW = [1., 1., 0., 1.]
TRANSPARENT_PURPLE = [1., 0., 1., 0.5]

if __name__=="__main__":
    '''
    TASK 1: INITIALIZE YOUR OBJECT
    1.1 You need to decide which object you want to create. Choose from a list of:
    - CUBE
    - WEIGHT
    - BEAR
    - DUCK
    and substitute that word in "object=" in the function below.

    1.2 Then, specify the object size with SMALL, MEDIUM, or BIG in the second argument.

    Now run this file from IDLE. Click and drag on the object to move it around. If it 
    disappears, it means you threw it into the nether. Relaunch to continue throwing 
    it around.
    '''

    my_object = initialize_object(object=CUBE, size=SMALL)

    '''
    TASK 2: CHANGE THE COLORS 
    Notice at the top of this file that RED, GREEN, and BLUE are each defined using
    a list of 4 numbers, where each number ranges from 0.0 to 1.0:

    [Red, Green, Blue, Alpha]

    This forms the RGBA color scheme. You have probably heard of RGB before 
    from art or science class: you can combine red, green, and blue to create
    any color. Alpha is simply tacked on to control transparency. For example,
    if I wanted a fully opaque red, I would want 100% red, 0% green, 0% blue,
    and 100% alpha:
            R    G    B    A
    RED = [1.0, 0.0, 0.0, 1.0]

    But if I wanted a semi-transparent purple, I would want 100% red, 0% green, 
    100% blue, and 50% alpha:
            R    G    B    A
    TRANSPARENT_PURPLE = [1.0, 0.0, 1.0, 0.5]

    2.1. Make the object that you created in task 1 change colors when you press 
    the space bar. All you need to do is add the colors defined at the top of 
    the file to the empty list of colors below, like so:

    colors = [RED, BLUE] # you can add more than 2 colors!

    When you run this file in the IDLE and press the space bar repeatedly, you should
    be able to cycle through all your colors.

    2.2. Now it's time to experiment with your own colors! Define your own RGBA
    color at the top of the file and then add it to the list of colors below, like so:

    colors = [RED, BLUE, YOUR_COLOR]

    Try out this link to help you pick colors: https://rgbacolorpicker.com/
    Note that the RGB defined in the link are from 0 to 255, instead of 
    0 to 1. Just divide the RGB you get from the link by 255 to get the 
    decimal value from 0 to 1 that you want. For example, if you like the 
    RGBA color from the link:

    [255, 200, 50, 1]

    Then just use:

    [255 / 255., 200 / 255., 50 / 255., 1]
    '''

    colors = []

    change_to_colors(colors=colors)

    '''
    TASK 3 Change physics parameters
    Here we will practice calling functions with different types of inputs. Try calling the following functions with these input types
    The first obvious one is gravity. 
    TODO QUESTION 1: Try to make the object go up and down. What values made the object go up? What made it go down?
    '''
    set_gravity_z_axis(0) #TODO replace 0 with another value, observe what happens

    '''
    TASK 4 Change the simulation step
    This type of simulation computes the physics at a particular level of precision.
    Ex) if the time step is 1 second, the simulator computes what will happen after 1 second. 
    TODO QUESTION 2: The lower the time step, generally, the better the precision. Try running the simulation with a different time step.
    What happens?
    '''
    set_simulation_time_step(1/240.)

    '''
    Set and get
    We have been setting some values. Next we will get a value and print it out. 
    TASK 5
    Uncomment this code and get it to set the pose of the object you created.
    TODO, set the object in 3 different locations and take a screenshot of the result.  
    '''
    my_point = (0,0,0)
    set_point(my_object, my_point)

    

