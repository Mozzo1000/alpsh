import json
import time
import os

location = os.path.expanduser('~') + "/.alpsh/"


def create():
    if not os.path.exists(location):
        os.makedirs(location)

    if not os.path.isfile(location + "alpsh_history.json"):
        data = {'history': []}
        with open(location + 'alpsh_history.json', 'w') as history:
            json.dump(data, history, indent=4)


def write(command):
    try:
        with open(location + 'alpsh_history.json') as history_read:
            data = json.load(history_read)
            filteredcommand = command.replace("\n", "")
        data['history'].append({
            'timestamp': time.strftime("%c"),
            'command': filteredcommand
        })
        with open(location + 'alpsh_history.json', 'w') as history:
            json.dump(data, history, indent=4)
    except(IOError, OSError) as e:
        print("File not found? : " + str(e))
