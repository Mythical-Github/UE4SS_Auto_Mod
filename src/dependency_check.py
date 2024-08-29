import os
import shutil
import subprocess

import log_py.log_py as log

def check_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
        return result.returncode == 0
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
    except UnicodeDecodeError as e:
        log.log_message(f"Error: {e}")
        return False

def check_rust():
    if check_command(["cargo", "--version"]):
        log.log_message("Check: Rust: Installed")
    else:
        log.log_message("Check: Rust: Not Installed")
        raise EnvironmentError("Check: Rust not installed and/or in path")

def check_msvc_build_tools():
    cl_path = shutil.which("cl.exe")
    if cl_path:
        log.log_message("Check: MSVC Build Tools: Installed")
        return True
    path_dirs = os.getenv("PATH", "").split(os.pathsep)
    for directory in path_dirs:
        full_path = f'{directory}/cl.exe'
        if os.path.isfile(full_path):
            log.log_message("Check: MSVC Build Tools: Installed")
            return True
    log.log_message("Check: MSVC Build Tools: Not Installed")
    raise EnvironmentError("Check: MSVC Build Tools not installed and/or in path")

def check_git():
    if check_command(["git", "--version"]):
        log.log_message("Check: Git: Installed")
    else:
        log.log_message("Check: Git: Not Installed")
        raise EnvironmentError("Check: Git not installed and/or in path")

def check_git_bash():
    if check_command(["bash", "--version"]):
        log.log_message("Check: Git Bash: Installed")
    else:
        log.log_message("Check: Git Bash: Not Installed")

def check_xmake():
    if check_command(["xmake", "--version"]):
        log.log_message("Check: xmake: Installed")
    else:
        log.log_message("Check: xmake: Not Installed")
        raise EnvironmentError("Check: xmake not installed and/or in path")

def check_all():
    log.log_message("Check: Checking installations...")
    
    check_rust()
    check_msvc_build_tools()
    check_git()
    check_xmake()
