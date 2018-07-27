import xdg.BaseDirectory
import sys
import os


_data_dir   = xdg.BaseDirectory.save_data_path('ocrscrot')
_config_dir = xdg.BaseDirectory.save_config_path('ocrscrot')
TEMP_FILE   = '/tmp/socr-temp-file'
PICKLE_PATH = os.path.join(_data_dir, 'screenshots.pickle')
sys.path.append(_config_dir)
try:
    config = __import__('config')
except ModuleNotFoundError:
    print('config file not found', file=sys.stderr)
    sys.exit(1)
SCREENSHOT_DIR = os.path.expanduser(config.SCREENSHOT_DIR)
_screenshot_ext = config.SCREENSHOT_EXT
SCROT_PATTERN  = os.path.join(SCREENSHOT_DIR, "*." + _screenshot_ext)
