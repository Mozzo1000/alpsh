import json
import time
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)
file = "alpsh_history.json"


def create():
    if not os.path.exists(LOCATION):
        os.makedirs(LOCATION)

    if not os.path.isfile(LOCATION + file):
        data = {'history': []}
        with open(LOCATION + file, 'w') as history:
            json.dump(data, history, indent=4)
    open(LOCATION + 'alpsh_history_tmp', 'w')


def get_file():
    return LOCATION + file


def get_plain_file():
    try:
        with open(LOCATION + file) as history_read:
            data = json.load(history_read)
        for command in data['history']:
            tmpfile = open(LOCATION + 'alpsh_history_tmp', 'a')
            tmpfile.write(command['command'] + "\n")
            tmpfile.close()
        return LOCATION + 'alpsh_history_tmp'
    except(IOError, OSError) as error:
        logger.error("File not found? : " + str(error))
        return None


def write(command, success=True):
    try:
        with open(LOCATION + file) as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'command': filteredcommand,
            'timestamp': time.strftime("%c"),
            'success': str(success)
        })
        with open(LOCATION + file, 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as error:
        logger.error("File not found? : " + str(error))
