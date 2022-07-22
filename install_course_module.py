import os
import sys
import subprocess

def run_pip(pip_args, *args, **kwargs):
    return subprocess.check_call([sys.executable, '-m', 'pip'] + pip_args, *args, **kwargs)

if __name__ == '__main__':
    run_pip(['uninstall', '-y', 'pybullet_arm_course'])
    this_dir = os.path.join(os.path.dirname(__file__), '.')
    run_pip(['install', '-e', this_dir])

