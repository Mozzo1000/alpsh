from alpsh.constants import *
from rapidtables import make_table
import os
import json
import alpsh.config as config
import alpsh.history as history_listener


def history(args):
    print("ARGS : " + str(args))
    # If no arguments typed
    if len(args) == 0:
        print("HOWTO")
    elif str(args[0]) == "list":
        # List history in order
        print("List history")
        with open(CONFIG_PATH + 'alpsh_history.json', 'r') as history_list:
            data = json.load(history_list)
            count = 0
            table = []
            history_data = data['history'][count]
            for item in range(len(data["history"])):
                table.append({'Index': str(count), 'Command': history_data['command'],
                              "Timestamp": history_data['timestamp'], 'Success': history_data['success']})
                count += 1
            tables = make_table(table, tablefmt='md')
            print(tables)
            print()
    elif str(args[0] == "clear"):
        print(config.get_setting('text', 'danger')+"-=-=-=-=-=-=-=-WARNING-=-=-=-=-=-=-=\n" +
              COLORS.CLEAR + "You are about to remove your command history.\n" +
              "This is generally not necessary and is not recommended to do without reason.\n" +
              config.get_setting('text', 'danger') + "-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=" + COLORS.CLEAR)
        response = input("Are you sure you want to continue? [y/N] ")
        if response == "y":
            # Remove history
            history_listener.create(reset=True)
            print(config.get_setting('text', 'warning') + "History cleared!\n" + COLORS.CLEAR)
        else:
            # Don't remove history
            print(config.get_setting('text', 'warning') + "Aborted!\n" + COLORS.CLEAR)

    return SHELL_STATUS_RUN
