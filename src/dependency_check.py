import subprocess

def check_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True, encoding='utf-8')
        return result.stdout.strip() if result.stdout else True
    except subprocess.CalledProcessError:
        return False
    except FileNotFoundError:
        return False
    except UnicodeDecodeError as e:
        print(f"Unicode decoding error: {e}")
        return False

def check_rust():
    return check_command(["cargo", "--version"])


def check_msvc_build_tools():
    return check_command(["cl", "/?"])


def check_git():
    return check_command(["git", "--version"])

def check_git_bash():
    return check_command(["bash", "--version"])

def check_xmake():
    return check_command(["xmake", "--version"])

def check_all():
    print("Checking installations...\n")
    
    rust_installed = check_rust()
    msvc_installed = check_msvc_build_tools()
    git_installed = check_git()
    git_bash_installed = check_git_bash()
    xmake_installed = check_xmake()
    
    print(f"Rust: {'Installed' if rust_installed else 'Not Installed'}")
    print(f"MSVC Build Tools: {'Installed' if msvc_installed else 'Not Installed'}")
    print(f"Git: {'Installed' if git_installed else 'Not Installed'}")
    print(f"Git Bash: {'Installed' if git_bash_installed else 'Not Installed'}")
    print(f"xmake: {'Installed' if xmake_installed else 'Not Installed'}")