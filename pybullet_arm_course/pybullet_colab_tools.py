import os
os.environ['MESA_GL_VERSION_OVERRIDE'] = '3.3'
os.environ['MESA_GLSL_VERSION_OVERRIDE'] = '330'
import pybullet as p
import pybullet_data as pd
import numpy as np

from numpngw import write_apng, write_png

def setup_pybullet_colab(verbose=False):
    p.connect(p.DIRECT)
    #allow to find the assets (URDF, obj, textures etc)
    p.setAdditionalSearchPath(pd.getDataPath())
    #optionally enable GPU for faster rendering in pybullet.getCameraImage
    enableGPU = False
    #import GPUtil as GPU
    import sys
    # Get all device ids and their processing and memory utiliazion
    # (deviceIds, gpuUtil, memUtil) = GPU.getGPUs()

    # Print os and python version information
    if verbose:
        print('OS: ' + sys.platform)
        print(sys.version)
        # Print package name and version number
        print(GPU.__name__ + ' ' + GPU.__version__)
        # Show the utilization of all GPUs in a nice table
        GPU.showUtilization()

        # Show all stats of all GPUs in a nice table
        GPU.showUtilization(all=True)

    # NOTE: If all your GPUs currently have a memory consumption larger than 1%,
    # this step will fail. It's not a bug! It is intended to do so, if it does not
    # find an available GPU.
    #GPUs = GPU.getGPUs()
    #numGPUs = len(GPU.getGPUs())
    numGPUs=1

    if numGPUs > 0:
        enableGPU = True
        eglPluginId = -1
    if enableGPU:
        import pkgutil
        egl = pkgutil.get_loader('eglRenderer')
        if (egl):
    	    eglPluginId = p.loadPlugin(egl.get_filename(), "_eglRendererPlugin")
        else:
            eglPluginId = p.loadPlugin("eglRendererPlugin")
    if verbose:
        if eglPluginId>=0:
            print("Using GPU hardware (eglRenderer)")  
        else:
            print("using CPU renderer (TinyRenderer)")


def make_scene():
    p.resetSimulation()
    p.configureDebugVisualizer(p.COV_ENABLE_GUI)
    useFixedBase = True
    flags = p.URDF_INITIALIZE_SAT_FEATURES
    plane_pos = [0,0,-0.625]
    plane = p.loadURDF("plane.urdf", plane_pos, flags = flags, useFixedBase=useFixedBase)
    table_pos = [0,0,-0.625]
    table = p.loadURDF("table/table.urdf", table_pos, flags = flags, useFixedBase=useFixedBase)
    xarm = p.loadURDF("xarm/xarm6_robot.urdf", flags = flags, useFixedBase=useFixedBase)
    xarm = p.loadURDF("laikago/laikago_toes.urdf", [1,0,-0.15],[0, 0.5, 0.5, 0], flags = flags, useFixedBase=useFixedBase)

def make_frame(yaw):
    camTargetPos = [0, 0, 0.3]
    cameraUp = [0, 0, 1]
    cameraPos = [1, 1, 1]
    pitch = -10.0
    roll = 0
    upAxisIndex = 2
    camDistance = 1.5
    pixelWidth = 320
    pixelHeight = 200
    nearPlane = 0.01
    farPlane = 100
    fov = 60
    viewMatrix = p.computeViewMatrixFromYawPitchRoll(camTargetPos, camDistance, yaw, pitch,
                                                                    roll, upAxisIndex)
    aspect = pixelWidth / pixelHeight
    projectionMatrix = p.computeProjectionMatrixFOV(fov, aspect, nearPlane, farPlane)
            
    img_arr = p.getCameraImage(pixelWidth,pixelHeight,viewMatrix,projectionMatrix)
    w = img_arr[0]  #width of the image, in pixels
    h = img_arr[1]  #height of the image, in pixels
    rgb = img_arr[2]  #color data RGB
    dep = img_arr[3]  #depth data
    #print("w=",w,"h=",h)
    np_img_arr = np.reshape(rgb, (h, w, 4))
    frame = np_img_arr[:, :, :3]
    return frame

def _generate_random_filename():
    random_number = np.random.randint(0,5000)
    image_name = f"example_{random_number}.png"
    return image_name

def make_single_image(image_name=None,angle=0):
    frame = make_frame(yaw=angle)
    if image_name is None:
        image_name = _generate_random_filename()
    write_png(image_name, frame)

def make_animation(image_name=None):
    frames=[] #frames to create animated png
    yaw = 0
    for r in range(60):
        yaw += 6
        frame = make_frame(yaw)
        frames.append(frame)
    print("creating animated png")
    if image_name is None:
        image_name = _generate_random_filename()
    write_apng(image_name, frames, delay=100)
    return image_name
