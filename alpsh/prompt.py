import alpsh.config as config
import getpass
import socket

altered_prompt = ""


def handle_prompt():
    global altered_prompt
    altered_prompt = config.get('general', 'prompt')
    if "@host" in config.get('general', 'prompt'):
        altered_prompt = altered_prompt.replace('@host', socket.gethostname())
    if "@user" in config.get('general', 'prompt'):
        altered_prompt = altered_prompt.replace('@user', getpass.getuser())


def get_prompt():
    return altered_prompt
