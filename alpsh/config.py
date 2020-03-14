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
        config.read_dict(DEFAULT_CONFIG_INI)

        with open(CONFIG_PATH + CONFIG_FILE, 'w') as config_file:
            config.write(config_file)


def get_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH + CONFIG_FILE)
    return config


def get_setting(section, setting, fallback=None):
    config = get_config()
    return config.get(section.upper(), setting, fallback=fallback)


def update_config(section, setting, value):
    config = get_config()
    config.set(section, setting, value)
    with open(CONFIG_PATH + CONFIG_FILE, 'w') as config_file:
        config.write(config_file)
