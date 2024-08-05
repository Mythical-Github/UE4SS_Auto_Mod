import sys
import json
from pathlib import Path

from python_logging import log
import commands
import ssh_check
import dependency_check
        

def app_setup_checks():
    log.log_message('Check: Checking environment is correctly setup...')
    dependency_check.check_all()
    ssh_check.check_ssh_key()

    
def cli_logic():
    if getattr(sys, 'frozen', False):
        script_dir = Path(sys.executable).parent
    else:
        script_dir = Path(__file__).resolve().parent

    cli_json = f'{script_dir}/cli.json'

    with open(cli_json, 'r') as file:
        cli_info_dict = json.load(file)

    args = sys.argv
    cli_args = sys.argv[1:]

    if len(sys.argv) < 2:
        log.log_message('Args:')
        for key in cli_info_dict.keys():
            log.log_message(f'Arg: {key}')
        sys.exit()

    if sys.argv[1] == '-h':
        log.log_message('Args:')
        for key in cli_info_dict.keys():
            log.log_message(f'Arg: {key}')
        sys.exit()

    if sys.argv[2] == '-h':
        arg = sys.argv[1]
        for entry_key in cli_info_dict:
            if entry_key == arg:
                arg_help_pairs_list = cli_info_dict[entry_key]['arg_help_pairs']
                log.log_message('Args:')
                for arg_help_dict in arg_help_pairs_list:
                    arg_help_dict_keys = list(arg_help_dict.keys())
                    if arg_help_dict_keys:
                        arg_name = arg_help_dict_keys[0]
                        arg_help = arg_help_dict[arg_name]
                        log.log_message(f'Arg: {arg_name}    Help: {arg_help}')
        sys.exit()

    for entry in cli_info_dict.keys():
        for arg in args:
            if arg == entry:
                function_name = cli_info_dict[entry]['function_name']
                if function_name:
                    function = getattr(commands, function_name)
                    log.log_message(f'Function: {function_name} was called')
                    log.log_message('Args:')
                    cli_args[0], cli_args[1] = cli_args[1], cli_args[0]
                    for arg in cli_args:
                        log.log_message(f'Arg: {arg}')
                    app_setup_checks()
                    function(*cli_args[1:])
