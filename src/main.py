#! /usr/bin/env python3
# coding: utf-8
"""gngn"""
import sys

import encryption.encryptor as crypt
import encryption.decryptor as dcrypt
import settings.colors as colors

import editor

color = colors.Colors()

def not_implemented():
    return print("Not yet implemented. Sorry :o")

def show_menu():
    """Display the inner menu"""
    # color.pprint("@", "reverse")
    color.pprint("cyan", "################## EREBUS - Simple Note Encryptor ##################")
    color.pprint("cyan", "--------------------------------------------------------------------")
    color.pprint("cyan", "    Press 'n' to start the editor (new file)                        ")
    color.pprint("cyan", "    Press 'o' to open a file and read content (Read-Only)           ")
    color.pprint("cyan", "    Press 'e' to edit a file (must exists)                           ")
    color.pprint("cyan", "    Press 'r' to erase files (DANGER)                               ")
    color.pprint("cyan", "    Press 'q' to quit Erebus                                         ")
    color.pprint("cyan", "---------------------------------------------------------------------")
    color.pprint("reset", "\n")

def main():
    """Main function"""
    while True:
        show_menu()
        choice = input("Option: ")
        if choice == 'n':
            color.pprint("reverse", "Stop text edition with Ctrl + D")
            color.pprint("reset", "---- BEGINING ----")
            file = editor.editor()
            file_to_encrypt = editor.save_file_to_encrypt(file)
            crypto = crypt.Encrypt(file_to_encrypt)
            crypto.encrypt()

        elif choice == 'o':
            file_name = input("File to open: ")
            color.pprint("reverse", "Opening {}".format(file_name))
            color.pprint("reset", "\n")
            crypted_file = dcrypt.Decrypt(file_name)

            crypted_file.decrypt_and_read()

        elif choice == 'e':
            not_implemented()
        elif choice == 'r':
            not_implemented()
        elif choice == 'q':
            color.pprint("green", "Goodbye ;)")
            color.pprint("reset", "\n")
            sys.exit()
        else:
            color.pprint("Bad option", "red")
        color.pprint("reset", "\n")

if __name__ == '__main__':
    main()
