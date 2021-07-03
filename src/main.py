#! /usr/bin/env python3
# coding: utf-8

import sys
import logging as lg
from os import getenv

import settings.settings as cfg
import encryption.encryptor as crypt

def editor():
    buffer = []
    clean_buff = []

    for line in sys.stdin:
        buffer.append(line)

    print("Exiting editor...")
    for ln in buffer:
        print(ln)

    if buffer is None:
        raise
    else:
        return buffer

def save_file_to_encrypt(file_content):
    home = getenv("HOME")
    settings = cfg.Config(home)
    file_name = input("File name : ")
    file_path = settings.WORKSPACE + file_name
    print(file_path)
    try:
        with open(file_path, "w+") as output_f:
            output_f.writelines(file_content)
    except FileNotFoundError as error:
        lg.critical("%s", error)
        raise FileNotFoundError
    print("Done.File saved at %s", file_path)
    return file_path

def show_menu():
    print("########## EREBUS - Simple file encryptor ##########")
    print("----------------------------------------------------")
    print("Press 'e' to start the editor")
    print("Press 'q' to quit Erebus")
    print("----------------------------------------------------")

def main():
    show_menu()
    while True:
        choice = input("Option: ")
        if choice == 'e':
            print("Stop text edition with Ctrl + D")
            file = editor()
            file_to_encrypt = save_file_to_encrypt(file)
            crypto = crypt.Encrypt(file_to_encrypt)
            crypto.encrypt()
        if choice == 'q':
            print("Exiting")
            sys.exit()

if __name__ == '__main__':
    main()