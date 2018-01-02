import yaml
import logging
from alpsh.constants import *

file = "config.yaml"

with open(LOCATION + file, 'r') as readFile:
    settings = yaml.load(readFile)


def create():
    if not os.path.exists(LOCATION):
        os.makedirs(LOCATION)
    if not os.path.isfile(LOCATION + file):
        open(LOCATION + file, 'w')


def reset_config():
    logging.debug("deleting everything and starting over!")
    template = {'general':{'output_color':'\033[1;32;45m'}}
    with open(LOCATION + file, 'w') as writeFile:
        yaml.dump(template, writeFile, default_flow_style=False)
