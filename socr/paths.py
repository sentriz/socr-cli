import xdg.BaseDirectory
import sys
import os
from config import Config


_data_dir   = xdg.BaseDirectory.save_data_path('socr')
_config_dir = xdg.BaseDirectory.save_config_path('socr')
TEMP_FILE   = '/tmp/socr-temp-file'
PICKLE_PATH = os.path.join(_data_dir, 'screenshots.pickle')
sys.path.append(_config_dir)
config_file = _config_dir + '/config.py'
config_parsed = Config(config_parsed)
#try:
#    config = __import__('config')
#except ModuleNotFoundError:
#    print('config file not found', file=sys.stderr)
#    sys.exit(1)
SCREENSHOT_DIR = os.path.expanduser(config_parsed.SCREENSHOT_DIR)
_screenshot_ext = config_parsed.SCREENSHOT_EXT
SCROT_PATTERN  = os.path.join(SCREENSHOT_DIR, "*." + _screenshot_ext)
