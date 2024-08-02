import subprocess
import log

def check_ssh_key():
    result = subprocess.run(
        ['ssh', '-T', 'git@github.com'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    
    message = str(result)
    if "You've successfully authenticated" in message:
        log.log_message("SSH keys are set up correctly.")
    else:
        log.log_message(message)