import sys
from pathlib import Path

import ssh_check
import dependency_check
from ue4ss_mod_build_tools import cli_py
from ue4ss_mod_build_tools.cli import OPTIONS
from ue4ss_mod_build_tools import log_py as log
from ue4ss_mod_build_tools.log_colors import COLORS


if getattr(sys, 'frozen', False):
    script_dir = Path(sys.executable).parent
else:
    script_dir = Path(__file__).resolve().parent


def app_setup_checks():
    log.log_message('Check: Checking environment is correctly setup...')
    dependency_check.check_all()
    ssh_check.check_ssh_key()


if __name__ == "__main__":
    try:
        log.set_log_base_dir(script_dir)
        log.set_colors_json_path(f'{script_dir}/json/log_colors.json')
        app_setup_checks()
        cli.set_json_location(f'{script_dir}/json/cli.json')
        cli.cli_logic()
    except Exception as error_message:
        log.log_message(str(error_message))     
