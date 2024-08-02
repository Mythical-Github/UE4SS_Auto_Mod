import os
import shutil
import subprocess

import log


def check_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
        return result.stdout.strip() if result.stdout else True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
    except UnicodeDecodeError as e:
        log.log_message(f"Error: {e}")
        return False


def check_rust():
    return check_command(["cargo", "--version"])


def check_msvc_build_tools():
    cl_path = shutil.which("cl.exe")
    if cl_path:
        return True
    path_dirs = os.getenv("PATH", "").split(os.pathsep)
    for directory in path_dirs:
        full_path = os.path.join(directory, "cl.exe")
        if os.path.isfile(full_path):
            return True
    return False


def check_git():
    return check_command(["git", "--version"])


def check_git_bash():
    return check_command(["bash", "--version"])


def check_xmake():
    return check_command(["xmake", "--version"])


def check_all():
    log.log_message("Check: Checking installations...")
    
    rust_installed = check_rust()
    msvc_installed = check_msvc_build_tools()
    git_installed = check_git()
    xmake_installed = check_xmake()
    
    log.log_message(f"Check: Rust: {'Installed' if rust_installed else 'Not Installed'}")
    log.log_message(f"Check: MSVC Build Tools: {'Installed' if msvc_installed else 'Not Installed'}")
    log.log_message(f"Check: Git: {'Installed' if git_installed else 'Not Installed'}")
    log.log_message(f"Check: xmake: {'Installed' if xmake_installed else 'Not Installed'}")

    # git_bash_installed = check_git_bash()
    # log.log_message(f"Git Bash: {'Installed' if git_bash_installed else 'Not Installed'}")
