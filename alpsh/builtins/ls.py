import os
from rapidtables import make_table
from alpsh.constants import *
import alpsh.utils as utils
import alpsh.config as config


def ls(args):
    # If there is any arguments typed
    if len(args) > 0:
        if args[0] == "walk":
            for root, dirs, files in os.walk("."):
                for filename in files:
                    print(filename)
        print("ARGS!")
        if os.path.isdir(args[0]):
            for link in os.listdir(args[0]):
                if not link.startswith('.'):
                    print(str(config.get('general', 'output_color')) + link + COLORS.CLEAR + ' ', end='')
            print()
        elif os.path.isfile(args[0]):
            print("Not a directory!")
    else:
        table = []
        for link in os.listdir(os.getcwd()):
            if not link.startswith('.'):
                full_path = os.getcwd() + "/" + link
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
    return SHELL_STATUS_RUN
