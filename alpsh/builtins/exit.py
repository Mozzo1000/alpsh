import os
from alpsh.constants import *


def exit(args):
    os.system('clear')
    print("Goodbye!")
    return SHELL_STATUS_STOP
