# -*- coding: utf-8 -*-

import shlex
import subprocess
import logging
import alpsh.history as history_listener
import alpsh.config as config
from alpsh.constants import *
from alpsh.builtins import *
import alpsh.prompt as prompt
import readline
import platform

# Hash map to store built-in function name and reference as key and value
built_in_cmds = {}
alias_in_cmds = {}
logger = logging.getLogger(__name__)


def shell_loop():
    # Start the loop here
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # Read the command input and display symbol
        cmd = input(prompt.get_prompt())

        # Tokenize the command input
        cmd_tokens = tokenize(cmd)

        # Execute the command and retrieve new status
        status = execute(cmd_tokens)


def tokenize(string):
    return shlex.split(string)


def execute(cmd_tokens):
    try:
        cmd_name = cmd_tokens[0]
        cmd_args = cmd_tokens[1:]

        if cmd_name in built_in_cmds:
            history_listener.write(" ".join(cmd_tokens))
            return built_in_cmds[cmd_name](cmd_args)
        elif cmd_name in alias_in_cmds:
            try:
                subprocess.call(tokenize(alias_in_cmds[cmd_name]))
            except FileNotFoundError:
                logger.info(str(tokenize(alias_in_cmds[cmd_name])) + " : Command not found!")
                print(str(tokenize(alias_in_cmds[cmd_name])) + " : Command not found!")
        elif config.get('general', 'open_if_file') == 'True' and os.path.isfile(cmd_name):
            if platform.system() == "Darwin":
                subprocess.call('open ' + cmd_name, shell=True)
        else:

            # Execute command
            try:
                subprocess.call(cmd_tokens)
                history_listener.write(" ".join(cmd_tokens))
            except subprocess.CalledProcessError as error:
                logger.error(error.output)
            except OSError as error:
                if "[Errno 2] No such file or directory:" in str(error):
                    logger.info(str(cmd_tokens[0]) + ": Command not found!")
                    print(str(cmd_tokens[0]) + ": Command not found!")
                    history_listener.write(" ".join(cmd_tokens), False)
                else:
                    logger.error(str(error))
    except IndexError as error:
        logger.debug("IndexError occurred : " + str(error))

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN


def register_command(name, func):
    built_in_cmds[name] = func


def register_alias():
    ALIAS_FILE_NAME = 'alias'
    if not os.path.isfile(LOCATION + ALIAS_FILE_NAME):
        with open(LOCATION + ALIAS_FILE_NAME, 'w') as alias_file:
            alias_file.write('alias=ls:ls --color=always')

    alias_file = open(LOCATION + ALIAS_FILE_NAME, 'r').readlines()
    for line in alias_file:
        alias_command = line.replace('alias=', '').replace("\n", '').split(':')
        alias_in_cmds[alias_command[0]] = alias_command[1]


def init():
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("history", history)
    if config.get('general', 'override_coreutils') == "True":
        register_command("ls", ls)
    register_alias()


def main():
    config.create()
    config.load()
    init()
    history_listener.create()  # Checks if the 'alpsh_history.json' file exists, if not it creates it.
    prompt.handle_prompt()
    readline.parse_and_bind('tab: complete')
    readline.read_history_file(history_listener.get_plain_file())
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)-12s/%(funcName)s():%(lineno)d - %(message)s', filename=LOCATION + 'alpsh.log', level=logging.DEBUG)
    shell_loop()


if __name__ == "__main__":
    main()
