import json
import os
import sys

import psutil

import enums

settings = ''
init_settings_done = False
settings_json_dir = ''
program_dir = ''
mod_names = []
settings_json = ''

if getattr(sys, 'frozen', False):
    SCRIPT_DIR = os.path.dirname(os.path.abspath(sys.executable))
else:
    SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
os.chdir(SCRIPT_DIR)


def init_settings(settings_json_path: str):
    global settings
    global init_settings_done
    global settings_json
    global settings_json_dir

    with open(settings_json_path, 'r') as file:
        settings = json.load(file)
    window_name = settings['general_info']['window_title']
    os.system(f'title {window_name}')
    init_settings_done = True
    settings_json = settings_json_path
    settings_json_dir = os.path.dirname(settings_json)
    return


def load_settings(settings_json: str):
    if not init_settings_done:
        init_settings(settings_json)
    with open(settings_json, 'r') as file:
        return json.load(file)


def save_settings(settings_json: str):
    with open(settings_json, 'w') as file:
        json.dump(settings, file, indent=2)


def pass_settings(settings_json: str):
    load_settings(settings_json)


def test_mods(settings_json: str, *input_mod_names: str):
    load_settings(settings_json)
    global mod_names
    for mod_name in input_mod_names:
        mod_names.append(mod_name)
    mods.create_mods()




def add_asset_paths_to_manually_specified_assets_in_mod_pak_info_entry(settings_json: str, mod_name: str,
                                                                       asset_paths: list):
    for info in settings["mod_pak_info"]:
        if info['mod_name'] == mod_name:
            for asset_path in asset_paths:
                info['manually_specified_assets']['asset_paths'].append(asset_path)
    save_settings(pass_settings(settings_json))
