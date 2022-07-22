import random
from pybullet_arm_course.environment_setup import *

'''
TASK 1: Run in IDLE

1.1. TODO: Run in IDLE

You should be able to press any key (preferably the space bar) and generate
ducks galore of different sizes! While this is pretty neat, this lab will 
walk you through generating random objects of random colors when you press
any key. Let's get started.
'''

RED = [1., 0., 0., 1.]
GREEN = [0., 1., 0., 1.]
BLUE = [0., 0., 1., 1.]
YELLOW = [1., 1., 0., 1.]
TRANSPARENT_PURPLE = [1., 0., 1., 0.5]

def uniform_size():
    return SMALL

def random_size():
    random_result = random.choice([SMALL, MEDIUM, BIG])
    return random_result

'''
TASK 2: Creating random objects

2.1 You need to create a list of objects from which the code will randomly 
choose one to generate. The possibilities:
    - CUBE
    - WEIGHT
    - BEAR
    - DUCK
Use the random_size() function, defined above, to help you write the function
"random_object()" below.

2.2. Then, replace "obj=uniform_object()" at the bottom of this page with
"obj=random_object()".

Run this program from the IDLE. Now you should be generating random objects
of different sizes when you press the space bar.s
'''

def random_object():
    raise NotImplementedError

'''
TASK 3: Creating random colors

2.1 You need to create a list of colors from which the code will randomly 
choose one to generate. The possibilities are defined at the top of the file.

Use the random_size() function, as well as the random_object function you just
wrote, to help you write the function "random_color()" below.

2.2. Then, replace "color=uniform_color()" at the bottom of this page with
"color=random_color()".

Now you should be generating random colors of different sizes when you press the space bar.

A QUICK ASIDE ABOUT CREATING YOUR OWN COLOR:
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

Try out this link to help you pick colors: https://rgbacolorpicker.com/
Note that the RGB defined in the link are from 0 to 255, instead of 
0 to 1. Just divide the RGB you get from the link by 255 to get the 
decimal value from 0 to 1 that you want. For example, if you like the 
RGBA color from the link:

[255, 200, 50, 1]

Then just use:

[255 / 255., 200 / 255., 50 / 255., 1]

2.3 Now, create your OWN color, using the colors defined at the top of this 
file to help you. Once you have created your own color, add it to the list
of random colors in the "random_color()" function. 
'''

def random_color():
    raise NotImplementedError

'''
Task 3: creating objects using for loops
Create different shapes of objects using set_point

Functions:
make_line: make a line of num_objects objects
make_grid: make an M by N grid spaced by 'spacing' units apart
make_tower: stack num_objects such that the tower does not collapse. There are many
possible solutions to this!
'''
def make_line(num_objects):
    pass

def make_grid(m, n, spacing):
    pass

def make_tower(num_objects):
    pass


if __name__=="__main__":
    initialize_environment()
    while simulation_is_running():
        if any_key_is_pressed():
            spawn_object(obj=uniform_object(), size=random_size(), color=uniform_color())
    #make_line(10)
    #make_grid(4,10,0.1)
    #make_tower(5)

