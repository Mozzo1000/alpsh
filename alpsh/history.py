import json
import time
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)


def create():
    if not os.path.exists(LOCATION):
        os.makedirs(LOCATION)

    if not os.path.isfile(LOCATION + HISTORY_FILE):
        data = {'history': []}
        with open(LOCATION + HISTORY_FILE, 'w') as history:
            json.dump(data, history, indent=4)
    open(LOCATION + HISTORY_FILE_TMP, 'w')


def get_file():
    return LOCATION + HISTORY_FILE


def get_plain_file():
    try:
        with open(LOCATION + HISTORY_FILE) as history_read:
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
        with open(LOCATION + HISTORY_FILE) as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'command': filteredcommand,
            'timestamp': time.strftime("%c"),
            'success': str(success)
        })
        with open(LOCATION + HISTORY_FILE, 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as error:
        logger.error("File not found? : " + str(error))
