import json
import time
import logging
from alpsh.constants import *

logger = logging.getLogger(__name__)


def create(reset=False):
    if not os.path.exists(CONFIG_PATH):
        os.makedirs(CONFIG_PATH)

    if not os.path.isfile(CONFIG_PATH + HISTORY_FILE) or reset is True:
        data = {'history': []}
        with open(CONFIG_PATH + HISTORY_FILE, 'w') as history:
            json.dump(data, history, indent=4)
    open(CONFIG_PATH + HISTORY_FILE_TMP, 'w')


def get_file():
    return CONFIG_PATH + HISTORY_FILE


def get_plain_file():
    try:
        with open(CONFIG_PATH + HISTORY_FILE) as history_read:
            data = json.load(history_read)
        for command in data['history']:
            tmpfile = open(CONFIG_PATH + 'alpsh_history_tmp', 'a')
            tmpfile.write(command['command'] + "\n")
            tmpfile.close()
        return CONFIG_PATH + 'alpsh_history_tmp'
    except(IOError, OSError) as error:
        logger.error("File not found? : " + str(error))
        return None


def write(command, success=True):
    try:
        with open(CONFIG_PATH + HISTORY_FILE) as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'command': filteredcommand,
            'timestamp': time.strftime("%c"),
            'success': str(success)
        })
        with open(CONFIG_PATH + HISTORY_FILE, 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as error:
        logger.error("File not found? : " + str(error))
