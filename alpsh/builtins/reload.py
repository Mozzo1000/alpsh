import os
import sys
from alpsh.constants import *


def reload(args):
    print(sys.version)
    os.execv(sys.executable, ['python'] + sys.argv)
    return SHELL_STATUS_STOP
