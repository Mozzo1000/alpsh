import json
import time
import os

location = os.path.expanduser('~') + "/.alpsh/"
file = "alpsh_history.json"


def create():
    if not os.path.exists(location):
        os.makedirs(location)

    if not os.path.isfile(location + file):
        data = {'history': []}
        with open(location + file, 'w') as history:
            json.dump(data, history, indent=4)
    open(location + 'alpsh_history_tmp', 'w')


def get_file():
    return location + file


def get_plain_file():
    try:
        with open(location + file) as history_read:
            data = json.load(history_read)
        for command in data['history']:
            tmpfile = open(location + 'alpsh_history_tmp', 'a')
            tmpfile.write(command['command'] + "\n")
            tmpfile.close()
        return location + 'alpsh_history_tmp'
    except(IOError, OSError) as e:
        print("File not found? : " + str(e))
        return None


def write(command):
    try:
        with open(location + file) as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'command': filteredcommand,
            'timestamp': time.strftime("%c")
        })
        with open(location + file, 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as e:
        print("File not found? : " + str(e))
