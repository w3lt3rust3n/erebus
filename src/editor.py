import sys
import logging as lg

from os import getenv

import settings.settings as cfg
import settings.colors as colors

colors = colors.Colors()

def editor():
    """Getting user input and return it."""
    buffer = []
    colors.pprint("green", "\n")
    for line in sys.stdin:
        buffer.append(line)
    colors.pprint("cyan", "Exiting editor...")

    if buffer is None:
        colors.pprint("reset", "!!")
        sys.exit()
    return buffer

def save_file_to_encrypt(file_content):
    """Save given buffer into file."""
    home = getenv("HOME")
    settings = cfg.Config(home)
    colors.pprint("reset", "\n")
    file_name = input("File name : ")
    file_path = settings.workspace + file_name

    try:
        with open(file_path, "w+") as output_f:
            output_f.writelines(file_content)
    except FileNotFoundError as error:
        lg.critical("%s", error)
        raise

    colors.pprint("green", "File saved !")
    return file_path