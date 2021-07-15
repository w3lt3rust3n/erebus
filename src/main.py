#! /usr/bin/env python3
# coding: utf-8
"""gngn"""
import sys

import encryption.encryptor as crypt
import encryption.decryptor as dcrypt

import editor

def show_menu():
    """gngn"""
    print("########## EREBUS - Simple file encryption ##########")
    print("-----------------------------------------------------")
    print("Press 'n' to start the editor (new file)")
    print("Press 'o' to open a file and read content (Read-Only)")
    print("Press 'e' to edit a file (must exists)")
    print("Press 'r' to erase files (DANGER)")
    print("Press 'q' to quit Erebus")
    print("-----------------------------------------------------")

def main():
    """gngn"""
    while True:
        show_menu()
        choice = input("Option: ")
        if choice == 'n':
            print("Stop text edition with Ctrl + D")
            file = editor.editor()
            file_to_encrypt = editor.save_file_to_encrypt(file)
            crypto = crypt.Encrypt(file_to_encrypt)
            crypto.encrypt()

        if choice == 'o':
            file_name = input("File to open: ")
            print("Opening {}".format(file_name))
            crypted_file = dcrypt.Decrypt(file_name)

            crypted_file.decrypt_and_read()
        
        if choice == 'e':
            pass
        if choice == 'r':
            pass
        if choice == 'q':
            print("Exiting")
            sys.exit()

if __name__ == '__main__':
    main()
