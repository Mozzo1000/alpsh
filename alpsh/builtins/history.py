from alpsh.constants import *
import os
import json


def history(args):
    print("ARGS : " + str(args))
    # If no arguments typed
    if len(args) == 0:
        print("HOWTO")
    elif str(args[0]) == "list":
        # List history in order
        print("List history")
        with open(LOCATION + 'alpsh_history.json', 'r') as history_list:
            data = json.load(history_list)
            count = 0
            for item in range(len(data["history"])):
                print("INDEX : " + str(count))
                print("COMMAND : " + data['history'][count]['command'])
                print("TIMESTAMP : " + data['history'][count]['timestamp'])
                print("SUCCESS : " + data['history'][count]['success'])
                count += 1
    elif str(args[0] == "clear"):
        data = {'history': []}
        with open(LOCATION + HISTORY_FILE, 'w') as history:
            json.dump(data, history, indent=4)
        open(LOCATION + HISTORY_FILE_TMP, 'w')

    return SHELL_STATUS_RUN
