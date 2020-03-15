import logging
from alpsh.constants import *
import configparser
import os

logger = logging.getLogger(__name__)


def create_config(reset=False):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)
    if not os.path.exists(CONFIG_PATH + CONFIG_FILE) or reset is True:
        config = configparser.ConfigParser()

        config.add_section('general')
        config.add_section('text')

        config.set('general', 'output_color', "'\033[1;32;45m'")
        config.set('general', 'prompt', '>')
        config.set('general', 'override_coreutils', 'False')
        config.set('general', 'open_if_file', 'True')
        config.set('general', 'show_default_shell_warning', 'True')
        config.set('text', 'danger', "'\033[1;31m'")
        config.set('text', 'warning', "'\033[1;33m'")

        with open(CONFIG_PATH + CONFIG_FILE, 'w') as config_file:
            config.write(config_file)


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH + CONFIG_FILE)
    return config


def get_setting(section, setting, fallback=None, isbool=False):
    config = get_config()
    if isbool is True:
        return config.getboolean(section.lower(), setting, fallback=fallback)
    else:
        return config.get(section.lower(), setting, fallback=fallback)


def update_config(section, setting, value):
    config = get_config()
    config.set(section, setting, value)
    with open(CONFIG_PATH + CONFIG_FILE, 'w') as config_file:
        config.write(config_file)
