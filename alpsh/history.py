import json
import time
import os
from alpsh.constants import *

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
    except(IOError, OSError) as e:
        print("File not found? : " + str(e))
        return None


def write(command):
    try:
        with open(LOCATION + file) as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'command': filteredcommand,
            'timestamp': time.strftime("%c")
        })
        with open(LOCATION + file, 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as e:
        print("File not found? : " + str(e))
