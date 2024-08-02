import os
import sys
import shutil

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)

BASE_DIR = os.path.normpath(os.path.join(SCRIPT_DIR, '..', 'base'))

cleanup_list = {
f'{SCRIPT_DIR}/dist',
f'{SCRIPT_DIR}/build',
f'{SCRIPT_DIR}/__main__.spec',
f'{BASE_DIR}/UnrealAutoMod'
}

for entry in cleanup_list:
    if os.path.isfile(entry):
        os.remove(entry)
    if os.path.isdir(entry):
        shutil.rmtree(entry)
