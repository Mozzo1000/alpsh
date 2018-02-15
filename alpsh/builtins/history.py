from alpsh.constants import *
import os
import json
import alpsh.config as config


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
        print(config.get('text', 'danger')+"-=-=-=-=-=-=-=-WARNING-=-=-=-=-=-=-=\n" +
              COLORS.CLEAR + "You are about to remove your command history.\n" +
              "This is generally not necessary and is not recommended to do without reason.\n" +
              config.get('text', 'danger') + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + COLORS.CLEAR)
        response = input("Are you sure you want to continue? [y/N] ")
        if response == "y":
            # Remove history
            data = {'history': []}
            with open(LOCATION + HISTORY_FILE, 'w') as history:
                json.dump(data, history, indent=4)
            open(LOCATION + HISTORY_FILE_TMP, 'w')
            print(config.get('text', 'warning') + "History cleared!\n" + COLORS.CLEAR)
        else:
            # Don't remove history
            print(config.get('text', 'warning') + "Aborted!\n" + COLORS.CLEAR)

    return SHELL_STATUS_RUN
