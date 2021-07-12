import sys
import logging as lg

from os import getenv

import settings.settings as cfg

def editor():
    """gngn"""
    buffer = []

    for line in sys.stdin:
        buffer.append(line)

    print("Exiting editor...")

    if buffer is None:
        sys.exit()
    return buffer

def save_file_to_encrypt(file_content):
    """gngn"""
    home = getenv("HOME")
    settings = cfg.Config(home)
    file_name = input("File name : ")
    file_path = settings.workspace + file_name

    try:
        with open(file_path, "w+") as output_f:
            output_f.writelines(file_content)
    except FileNotFoundError as error:
        lg.critical("%s", error)
        raise

    print("Done.File saved at {}".format(file_path))
    return file_path