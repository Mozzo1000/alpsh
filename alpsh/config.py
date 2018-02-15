import yaml
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)

file = "config.yaml"
settings = {}


def load():
    global settings
    try:
        readfile = open(LOCATION + file, 'r')
        settings = yaml.load(readfile)
        readfile.close()
    except IOError as error:
        logger.error(str(error))
    except yaml.YAMLError as exc:
        if hasattr(exc, 'problem_mark'):
            mark = exc.problem_mark
            logger.error("YAML Error : Position: (%s:%s)" % (mark.line+1, mark.column+1))
        print("Can't load config file. Using default")
        settings = {'general':{'output_color':'\033[1;32;45m', 'prompt':'>'}, 'text':{'danger':'\e[1;31m', 'warning':'\e[1;33m'}}


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
    template = {'general':{'output_color':'\033[1;32;45m', 'prompt':'>'}, 'text':{'danger':'\e[1;31m',
                                                                                  'warning':'\e[1;33m'}}
    with open(LOCATION + file, 'w') as writeFile:
        yaml.dump(template, writeFile, default_flow_style=False)
