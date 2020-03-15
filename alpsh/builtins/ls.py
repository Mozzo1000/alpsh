import os
from rapidtables import make_table
from alpsh.constants import *
import alpsh.utils as utils
import alpsh.config as config


def ls(args):
    # If there is any arguments typed
    if len(args) > 0:
        if os.path.isdir(args[0]):
            print_table(args[0])
        elif os.path.isfile(args[0]):
            print("Not a directory!")
    else:
        print_table(os.getcwd())
    return SHELL_STATUS_RUN


def print_table(directory):
    table = []
    for link in os.listdir(directory):
        if not link.startswith('.'):
            full_path = directory + "/" + link
            size = os.path.getsize(full_path)
            if os.path.isdir(full_path):
                file_type = "Directory"
            elif os.path.isfile(full_path):
                file_type = "File"
            else:
                file_type = "Unknown"
            table.append({'Name': link, 'Size': utils.convert_byte_size(size), "Type": file_type})

    tables = make_table(table, tablefmt='md')
    print(tables)
    print()
