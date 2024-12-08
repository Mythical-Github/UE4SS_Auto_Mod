from enum import Enum


class ScriptStateType(Enum):
    """
    enum for the various script states, used to fire off other functions
    at specific times
    """
    NONE = 'none'
    PRE_ALL = 'pre_all'
    POST_ALL = 'post_all'
    CONSTANT = 'constant'
    PRE_INIT = 'pre_init'
    INIT = 'init'
    POST_INIT = 'post_init'


class ExecutionMode(Enum):
    """
    enum for how to execute various processes
    """
    SYNC = 'sync'
    ASYNC = 'async'
    

class FileFilterType(Enum):
    """
    enum for how to include various files for mod creation functions
    """
    ASSET_PATHS = 'asset_paths'  # Takes the paths and gets all files regardless of extension
    TREE_PATHS = 'tree_paths'  # Takes supplied dirs, and traverses it all, including every file


def get_enum_from_val(enum: Enum, value: str) -> Enum:
    """
    """
    for member in enum:
        if member.value == value:
            return member
    return None
