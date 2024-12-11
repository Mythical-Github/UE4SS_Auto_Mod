import os

from ue4ss_mod_build_tools import log_py as log
from ue4ss_mod_build_tools import utilities
from ue4ss_mod_build_tools import settings

def package_mods():
    log.log_message('Function: package mods was called')

def package_mods(mod_names: list):
    log.log_message(f'Function: package mods with mod names {mod_names} was called')

def build_mods_all():
    log.log_message('Function: build mods all was called')

def build_mods(mod_names: list):
    log.log_message(f'Function: build mods with mod names {mod_names} was called')

def install_mods_all():
    log.log_message('Function: install mods all was called')

def install_mods(mod_names: list):
    log.log_message(f'Function: install mods with mod names {mod_names} was called')

def uninstall_mods_all():
    log.log_message('Function: uninstall mods all was called')

def uninstall_mods(mod_names: list):
    log.log_message(f'Function: uninstall mods with mod names {mod_names} was called')

def test_mods():
    log.log_message('Function: test mods was called')

def test_mods_all(settings_json: str):
    utilities.clone_ue4ss()
    os.chdir(f'{settings.SCRIPT_DIR}/RE-UE4SS')
    utilities.recursively_update_ue4ss_submodules()
    utilities.generate_vs_project()
    utilities.build_project()

def add_mod(mod_name: str):
    log.log_message(f'Function: add mod with mod name {mod_name} was called')

def add_mods(mod_names: list):
    log.log_message(f'Function: add mods with mod names {mod_names} was called')

def remove_mod(mod_name: str):
    log.log_message(f'Function: remove mod with mod name {mod_name} was called')

def remove_mods(mod_names: list):
    log.log_message(f'Function: remove mods with mod names {mod_names} was called')

def add_mod_from_repo_url(url: str):
    log.log_message(f'Function: add mod from repo url with url of {url} was called')

def add_mods_from_repo_urls(urls: list):
    log.log_message(f'Function: add mods from repo urls with a list of urls {urls} was called')
