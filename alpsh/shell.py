import shlex
import subprocess
import sys

import alpsh.history as history_listener
from alpsh.constants import *
from alpsh.builtins import *

# Hash map to store built-in function name and reference as key and value
built_in_cmds = {}


def shell_loop():
    # Start the loop here
    status = SHELL_STATUS_RUN

    while status == SHELL_STATUS_RUN:
        # Display a command prompt
        sys.stdout.write('>')
        sys.stdout.flush()

        # Read the command input
        cmd = sys.stdin.readline()

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
        print("ERROR : " + error.output)
    except OSError as error:
        print("ERROR 2 : " + str(error))

    # Return status indicating to wait for next command in shell_loop
    return SHELL_STATUS_RUN


def register_command(name, func):
    built_in_cmds[name] = func


def init():
    register_command("cd", cd)
    register_command("exit", exit)
    register_command("history", history)


def main():
    init()
    history_listener.create()  # Checks if the 'alpsh_history.json' file exists, if not it creates it.
    shell_loop()


if __name__ == "__main__":
    main()
