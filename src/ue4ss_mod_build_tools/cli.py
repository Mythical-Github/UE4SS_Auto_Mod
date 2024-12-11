from ue4ss_mod_build_tools import commands

OPTIONS = {
    "module": commands,
    "commands": {
        "package_mods_all": {
            "function_name": "package_mods_all",
            "arg_help_pairs": []
        },
        "package_mods": {
            "function_name": "package_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "build_mods_all": {
            "function_name": "build_mods_all",
            "arg_help_pairs": []
        },
        "build_mods": {
            "function_name": "build_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "install_mods_all": {
            "function_name": "install_mods_all",
            "arg_help_pairs": []
        },
        "install_mods": {
            "function_name": "install_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "uninstall_mods_all": {
            "function_name": "uninstall_mods_all",
            "arg_help_pairs": []
        },
        "uninstall_mods": {
            "function_name": "uninstall_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "test_mods_all": {
            "function_name": "test_mods_all",
            "arg_help_pairs": []
        },
        "test_mods": {
            "function_name": "test_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "add_mod": {
            "function_name": "add_mod",
            "arg_help_pairs": [
                {"mod_name": "Name of the mod to add"}
            ]
        },
        "add_mods": {
            "function_name": "add_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "remove_mod": {
            "function_name": "remove_mod",
            "arg_help_pairs": [
                {"mod_name": "Name of the mod to remove"}
            ]
        },
        "remove_mods": {
            "function_name": "remove_mods",
            "arg_help_pairs": [
                {"mod_names": "List of mod names, strings"}
            ]
        },
        "add_mod_from_repo_url": {
            "function_name": "add_mod_from_repo_url",
            "arg_help_pairs": [
                {"mod_name": "url of the repo to add"}
            ]
        },
        "add_mods_from_repo_urls": {
            "function_name": "add_mods_from_repo_urls",
            "arg_help_pairs": [
                {"mod_names": "List of repo urls to add, strings"}
            ]
        }
    }
}
