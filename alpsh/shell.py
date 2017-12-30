# -*- coding: utf-8 -*-

import shlex
import subprocess
import logging
import alpsh.history as history_listener
from alpsh.constants import *
from alpsh.builtins import *
import readline

# Hash map to store built-in function name and reference as key and value
built_in_cmds = {}
logger = logging.getLogger(__name__)


def shell_loop():
    # Start the loop here
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # Read the command input and display symbol
        cmd = input('>')

        # Tokenize the command input
        cmd_tokens = tokenize(cmd)

        # Execute the command and retrieve new status
        status = execute(cmd_tokens)
        history_listener.write(cmd)


def tokenize(string):
    return shlex.split(string)


def execute(cmd_tokens):
    cmd_name = cmd_tokens[0]
    cmd_args = cmd_tokens[1:]

    if cmd_name in built_in_cmds:
        return built_in_cmds[cmd_name](cmd_args)

    # Execute command
    try:
        subprocess.call(cmd_tokens)
    except subprocess.CalledProcessError as error:
        logger.error(error.output)
    except OSError as error:
        if str(error) == str("[Errno 2] No such file or directory: '" + str(cmd_tokens[0]) + "'"):
            logger.info(str(cmd_tokens[0]) + ": Command not found!")
            print(str(cmd_tokens[0]) + ": Command not found!")
        else:
            logger.error(str(error))

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN


def register_command(name, func):
    built_in_cmds[name] = func


def init():
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("history", history)
    register_command("ls", ls)


def main():
    init()
    history_listener.create()  # Checks if the 'alpsh_history.json' file exists, if not it creates it.
    readline.parse_and_bind('tab: complete')
    readline.read_history_file(history_listener.get_plain_file())
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)-12s/%(funcName)s():%(lineno)d - %(message)s', filename=LOCATION + 'alpsh.log', level=logging.DEBUG)
    shell_loop()


if __name__ == "__main__":
    main()
