from alpsh.constants import *
import getpass
import socket
import os
import subprocess
import shlex
import re
import logging
from pathlib import Path
import alpsh.utils as utils
import alpsh.config as config


logger = logging.getLogger(__name__)
altered_prompt = ""


def handle_prompt():
    global altered_prompt
    altered_prompt = config.get_setting('GENERAL', 'prompt')
    if "@host" in config.get_setting('GENERAL', 'prompt'):
        altered_prompt = altered_prompt.replace('@host', socket.gethostname())
    if "@user" in config.get_setting('GENERAL', 'prompt'):
        altered_prompt = altered_prompt.replace('@user', getpass.getuser())
    if "@dir" in config.get_setting('GENERAL', 'prompt'):
        altered_prompt = altered_prompt.replace('@dir', os.path.split(os.getcwd())[1])
    if "@fulldir" in config.get_setting('GENERAL', 'prompt'):
        altered_prompt = altered_prompt.replace('@fulldir', os.getcwd())
    if "@shortdir" in config.get_setting('general', 'prompt'):
        altered_prompt = altered_prompt.replace('@shortdir', str(Path(*Path(os.getcwd()).parts[-config.get_setting('prompt', 'short_directory_length', fallback=4):])))

def get_prompt():
    return altered_prompt


def default_shell():
    try:
        if utils.get_os() == "Darwin":
            shell = subprocess.check_output('dscl . -read /Users/' + getpass.getuser() + ' UserShell', shell=True)
            def_shell = shlex.split(shell.decode('utf-8'))[1]

        elif utils.get_os() == "Linux":
            file = open('/etc/passwd')
            for line in file:
                if re.search(getpass.getuser(), line):
                    def_shell = line.split(':')[-1].replace('\n', '')

        elif not utils.get_os():
            def_shell = default_shell_error_message
        else:
            def_shell = "NOT IMPLEMENTED!"
    except:
        logger.debug(default_shell_error_message)
        def_shell = default_shell_error_message

    if def_shell != utils.get_alpsh_installation():
        if config.get_setting('GENERAL', 'show_default_shell_warning', isbool=True) is True:
            print(config.get_setting('TEXT', 'warning') + '=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\nCURRENT DEFAULT SHELL IS : ' +
                  def_shell + '\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-' + COLORS.CLEAR)

