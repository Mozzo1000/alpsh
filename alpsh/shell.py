# -*- coding: utf-8 -*-

import shlex
import subprocess
import logging
import alpsh.history as history_listener
import alpsh.config as config
from alpsh.constants import *
from alpsh.builtins import *
from alpsh.utils import split_pipes
import alpsh.prompt as prompt
import alpsh.signals as signals
import readline
import platform
import os
import time

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

        if any('~' in word for word in cmd_args):
            logger.debug('Expanding tilde')
            cmd_tokens[1:] = [args.replace('~', os.path.expanduser('~')) for args in cmd_tokens[1:]]

        if '|' in cmd_tokens:
            pipeline = split_pipes(cmd_tokens)
            procs = [subprocess.Popen(pipeline[0], stdout=subprocess.PIPE)]
            time.sleep(0.1)
            for index, cmd in enumerate(pipeline):
                if index == 0:
                    continue
                elif index < len(pipeline) - 1:
                    procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout, stdout=subprocess.PIPE))
                else:
                    procs.append(subprocess.Popen(cmd, stdin=procs[index-1].stdout))
                time.sleep(0.1)

            procs[0].communicate()
            procs[-1].wait()

        elif cmd_name in built_in_cmds:
            history_listener.write(" ".join(cmd_tokens))
            return built_in_cmds[cmd_name](cmd_args)
        elif cmd_name in alias_in_cmds:
            try:
                subprocess.call(tokenize(alias_in_cmds[cmd_name]))
            except FileNotFoundError:
                logger.info(str(tokenize(alias_in_cmds[cmd_name])) + " : Command not found!")
                print(str(tokenize(alias_in_cmds[cmd_name])) + " : Command not found!")
        elif config.get_setting('general', 'open_if_file', isbool=True) is True and os.path.isfile(cmd_name):
            if platform.system() == "Darwin":
                subprocess.call('open ' + cmd_name, shell=True)
        elif os.path.isdir(cmd_name):
            os.chdir(cmd_name)
            prompt.handle_prompt()
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
    if not os.path.isfile(CONFIG_PATH + ALIAS_FILE_NAME):
        with open(CONFIG_PATH + ALIAS_FILE_NAME, 'w') as alias_file:
            alias_file.write('alias=ls:ls --color=always')

    alias_file = open(CONFIG_PATH + ALIAS_FILE_NAME, 'r')
    for line in alias_file.readlines():
        alias_command = line.replace('alias=', '').replace("\n", '').split(':')
        alias_in_cmds[alias_command[0]] = alias_command[1]
    alias_file.close()


def init():
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("history", history)
    register_command('reload', reload)
    if config.get_setting('general', 'override_coreutils') == "True":
        register_command("ls", ls)
    register_alias()


def main():
    signals.register_signals()
    config.create_config()
    init()
    history_listener.create()  # Checks if the 'alpsh_history.json' file exists, if not it creates it.
    prompt.default_shell()
    prompt.handle_prompt()
    readline.parse_and_bind('tab: complete')
    readline.read_history_file(history_listener.get_plain_file())
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)-12s/%(funcName)s():%(lineno)d - %(message)s', filename=CONFIG_PATH + 'alpsh.log', level=logging.DEBUG)
    shell_loop()


if __name__ == "__main__":
    main()
