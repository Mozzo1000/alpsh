import yaml
import logging
from alpsh.constants import *

file = "config.yaml"
settings = {}


def load():
    global settings
    try:
        readfile = open(LOCATION + file, 'r')
        settings = yaml.load(readfile)
        readfile.close()
    except IOError as error:
        logging.error(str(error))


def get(head, sub=None):
    return settings[head][sub]


def create():
    if not os.path.exists(LOCATION):
        os.makedirs(LOCATION)
    if not os.path.isfile(LOCATION + file):
        open(LOCATION + file, 'w')
        reset_config()


def reset_config():
    logging.debug("deleting everything and starting over!")
    template = {'general':{'output_color':'\033[1;32;45m', 'prompt':'>'}}
    with open(LOCATION + file, 'w') as writeFile:
        yaml.dump(template, writeFile, default_flow_style=False)
