import os

SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1

LOCATION = os.path.expanduser('~') + "/.alpsh/"


class COLORS:
    GREEN = '\033[1;32;45m'
    CLEAR = '\033[0m'
