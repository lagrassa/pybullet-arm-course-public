import os
import pybullet
import pybullet_arm_course as pac

def find_course_module():
    module_path = os.path.dirname(pac.__file__)

def position_string_to_position(position_string):
    #clean up some obvious symbols
    for stop_word in ["[", "]", "(", ")"," "]:
        position_string = position_string.replace(stop_word, "")
    split_by_commas = position_string.split(",")

    print(split_by_commas)
    values =  [float(value) for value in split_by_commas]
    if len(values) != 3:
        print("Number of values inputted in not equal to 3")
    else:
        return values


def wait_and_get_pressed_key():
    while True:
        keys = pybullet.getKeyboardEvents()
        for (key, value) in keys.items():
            print("Value", value)
            if value&pybullet.KEY_WAS_TRIGGERED:
                key_pressed = chr(key)
                return key_pressed
            

