import os

SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1

LOCATION = os.path.expanduser('~') + "/.alpsh/"
HISTORY_FILE = 'alpsh_history.json'
HISTORY_FILE_TMP = 'alpsh_history_tmp'

DEFAULT_CONFIG = {'general':{'output_color':'\033[1;32;45m', 'prompt':'>'}, 'text':{'danger':'\e[1;31m', 'warning':'\e[1;33m'}}


class COLORS:
    CLEAR = '\033[0m'
