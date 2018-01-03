import os
from alpsh.constants import *
import alpsh.config as config


def ls(args):
    # If there is any arguments typed
    if len(args) > 0:
        if args[0] == "walk":
            for root, dirs, files in os.walk("."):
                for filename in files:
                    print(filename)
        print("ARGS!")
    else:
        print("LIST DIR : " + os.getcwd())
        for link in os.listdir(os.getcwd()):
            if not link.startswith('.'):
                print(str(config.get('general', 'output_color')) + link + COLORS.CLEAR + ' ', end='')
        print()
    return SHELL_STATUS_RUN
