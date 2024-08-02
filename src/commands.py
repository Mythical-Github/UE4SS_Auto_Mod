import log
import settings

def test_mods():
    log.log_message('test mods was called')


def test_mods_all(settings_json: str):
    log.log_message('test mods all was called')
