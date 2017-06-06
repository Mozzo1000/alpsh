import json
import time


def create():
    data = {'history': []}
    with open('alpsh_history.json', 'w') as history:
        json.dump(data, history, indent=4)


def write(command):
    with open('alpsh_history.json') as history_read:
        data = json.load(history_read)
        filteredcommand = command.replace("\n", "")
    data['history'].append({
        'timestamp': time.strftime("%c"),
        'command': filteredcommand
    })
    with open('alpsh_history.json', 'w') as history:
        json.dump(data, history, indent=4)
