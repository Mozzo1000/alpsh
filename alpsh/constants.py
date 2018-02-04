import os

SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1

LOCATION = os.path.expanduser('~') + "/.alpsh/"
HISTORY_FILE = 'alpsh_history.json'
HISTORY_FILE_TMP = 'alpsh_history_tmp'


class COLORS:
    CLEAR = '\033[0m'
