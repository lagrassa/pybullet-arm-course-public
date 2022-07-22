import io
import os
import sys
import glob
import hashlib
import zipfile
import tempfile
import subprocess
import urllib.request

WINDOWS_WHEELS_URL = "http://www.andrew.cmu.edu/user/jgrosen/pybullet-wheels.zip"
WINDOWS_WHEEL_HASH = "3ddd5b333ad522eff3348dc89f59e4a117a06948e482944177002ca3892cd682"
CPP_REDIST_HELP = """
You'll have to install the Microsoft Visual C++ Redistributable, which you can do from this link:
https://support.microsoft.com/en-us/topic/the-latest-supported-visual-c-downloads-2647da03-1eea-4433-9aff-95f26a218cc0
You'll have to download the appropriate installer, then install it using administrative permissions, then come back and re-run this script.
"""

def run_pip(pip_args, *args, **kwargs):
    return subprocess.check_call([sys.executable, '-m', 'pip'] + pip_args, *args, **kwargs)

def are_deps_installed():
    try:
        import pybullet
        return True
    except ImportError:
        return False

def is_cpp_redist_installed():
    # assumes we're on windows
    import winreg
    try:
        redist_path = "SOFTWARE\\WOW6432Node\\Microsoft\\VisualStudio\\14.0\\VC\\Runtimes\\X64"
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, redist_path) as redist_key:
            installed_val, _ = winreg.QueryValueEx(redist_key, "Installed")
            return bool(installed_val)
    except FileNotFoundError:
        return False

def sha256hash(b):
    m = hashlib.sha256()
    m.update(b)
    return m.hexdigest()

def install_deps_windows():
    if not is_cpp_redist_installed():
        print(CPP_REDIST_HELP)
        sys.exit(1)

    # download the wheels
    print("Downloading wheels for Windows...")
    wheels_zip = urllib.request.urlopen(WINDOWS_WHEELS_URL).read()
    if sha256hash(wheels_zip) != WINDOWS_WHEEL_HASH:
        raise ValueError("Downloaded wheels zip seems to be corrupted")
    # unfortunately HTTPResponse is not file-like enough for ZipFile
    archive = zipfile.ZipFile(io.BytesIO(wheels_zip))
    with tempfile.TemporaryDirectory() as wheel_dir:
        archive.extractall(path=wheel_dir)

        # install the wheels
        print("Installing wheels...")
        wheels = glob.glob(os.path.join(wheel_dir, "wheels/*.whl"))
        run_pip(['install'] + wheels)

def install_deps_other():
    try:
        run_pip(['install', 'pybullet'])
    except subprocess.CalledProcessError:
        # probably not in a virtualenv, install using --user
        print("\nnormal install failed, trying user install\n")
        run_pip(['install', '--user', 'pybullet'])


if __name__ == '__main__':
    if not are_deps_installed():
        print("Installing dependencies...")
        run_pip(['uninstall', '-y', 'pybullet', 'pybullet_planning'])
        if os.name == 'nt':
            install_deps_windows()
        else:
            install_deps_other()
        print("Dependencies installed!")
    else:
        print("Looks like dependencies are already installed.")
