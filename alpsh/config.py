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
        settings = DEFAULT_CONFIG


def get(head, sub=None):
    if sub is None:
        return settings[head]
    else:
        return settings[head][sub]


def create():
    if not os.path.exists(LOCATION):
        os.makedirs(LOCATION)
    if not os.path.isfile(LOCATION + file):
        open(LOCATION + file, 'w')
        reset_config()


def reset_config():
    logging.debug("deleting everything and starting over!")

    with open(LOCATION + file, 'w') as writeFile:
        yaml.dump(DEFAULT_CONFIG, writeFile, default_flow_style=False)
