import os

SHELL_STATUS_STOP = 0
SHELL_STATUS_RUN = 1

CONFIG_PATH = os.path.expanduser('~/.alpsh/')
CONFIG_FILE = 'config.ini'
HISTORY_FILE = 'alpsh_history.json'
HISTORY_FILE_TMP = 'alpsh_history_tmp'

DEFAULT_CONFIG_INI = {'GENERAL': {
                        'output_color': '\033[1;32;45m',
                        'prompt': '>',
                        'override_coreutils': False,
                        'open_if_file': True
                    },
                    'TEXT': {
                        'danger': '\033[1;31m',
                        'warning': '\033[1;33m'
                    }}


class COLORS:
    CLEAR = '\033[0m'
