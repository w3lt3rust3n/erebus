#! /usr/bin/env python3
# coding: utf-8
"""gngn"""
import sys

import encryption.encryptor as crypt

import editor

def show_menu():
    """gngn"""
    print("########## EREBUS - Simple file encryption ##########")
    print("-----------------------------------------------------")
    print("Press 'e' to start the editor")
    print("Press 'q' to quit Erebus")
    print("-----------------------------------------------------")

def main():
    """gngn"""
    show_menu()
    while True:
        choice = input("Option: ")
        if choice == 'e':
            print("Stop text edition with Ctrl + D")
            file = editor.editor()
            file_to_encrypt = editor.save_file_to_encrypt(file)

            crypto = crypt.Encrypt(file_to_encrypt)
            crypto.encrypt()
        if choice == 'q':
            print("Exiting")
            sys.exit()

if __name__ == '__main__':
    main()
