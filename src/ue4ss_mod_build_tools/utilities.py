import os
import subprocess

from ue4ss_mod_build_tools.enums import ExecutionMode
from ue4ss_mod_build_tools import log_py as log


def run_app(exe_path: str, exec_mode: ExecutionMode = ExecutionMode.SYNC, args: list = [], working_dir: str = None):
    if exec_mode == ExecutionMode.SYNC:
        command = exe_path
        for arg in args:
            command = f'{command} {arg}'
        if working_dir:
            command = f'{working_dir}/{command}'
        log.log_message(f'Command: {command} running with the {exec_mode} enum')
        if working_dir:
            if os.path.isdir(working_dir):
                os.chdir(working_dir)

        process = subprocess.Popen(command, cwd=working_dir, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, shell=True)
        
        for line in iter(process.stdout.readline, ''):
            log.log_message(line.strip())

        process.stdout.close()
        process.wait()
        log.log_message(f'Command: {command} finished')


def build_project():
    app_args = [
        'build'
    ]
    app_command = 'xmake'
    run_app(exe_path=app_command, args=app_args)  


def generate_vs_project():
    log.log_message('Log: Generating Project')
    run_app('xmake project --kind=vsxmake2022 "--modes=Game__Shipping__Win64" -y')
    log.log_message('Log: Finished Generating Project')    


def recursively_update_ue4ss_submodules():
    app_args = [
        'submodule',
        'update',
        '--init',
        "--recursive",
    ]
    app_command = 'git'
    run_app(exe_path=app_command, args=app_args)    


def clone_ue4ss():
    ue4ss_clone_command = 'git@github.com:UE4SS-RE/RE-UE4SS.git'
#     ue4ss_clone_command = 'git@github.com:Mythical-Github/RE-UE4SS.git'

    app_args = [
        'clone',
        ue4ss_clone_command
    ]
    app_command = 'git'
    run_app(exe_path=app_command, args=app_args)
