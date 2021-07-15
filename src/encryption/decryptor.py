#! /usr/bin/env python3
# coding: utf-8

"""lorem"""
# import required module
from os import getenv

from cryptography.fernet import Fernet

import settings.settings as cfg
import encryption.encryptor as crypt
import settings.colors as colors

colors = colors.Colors()

class Decrypt:
    """All that Erebus needs to encrypt notes."""
    def __init__(self, file_to_decrypt):
        self.encrypted_file = file_to_decrypt
        self.home = getenv('HOME')
        self.config = cfg.Config(self.home)

    @classmethod
    def __close_and_encrypt(cls, file_to_close):
        crypto = crypt.Encrypt(file_to_close)
        crypto.encrypt()

    def get_key(self):
        """Open a given key file to open and return it"""
        key_directory = self.config.get_key_dir()
        key_filename = key_directory + self.encrypted_file + ".key"
        colors.pprint("cyan", "Opening the key")
        with open(key_filename, 'rb') as filekey:
            key = filekey.read()
        return key

    def decrypt_and_read(self):
        """Decrypt the file and print its content on screen"""
        file_to_decrypt = self.encrypted_file
        workspace = self.config.get_workspace()
        path_to_file = workspace + file_to_decrypt

        colors.pprint("cyan", "Getting key")
        key = self.get_key()
        colors.pprint("cyan", "Using key")
        fernet = Fernet(key)

        colors.pprint("cyan", "Reading encrypted file")
        with open(path_to_file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()

        colors.pprint("cyan", "Decrypting the content")
        decrypted = fernet.decrypt(encrypted)

        colors.pprint("cyan", "Writing decrypted content")
        with open(path_to_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)

        colors.pprint("cyan", "Displaying file content")
        with open(path_to_file, 'r') as file:
            output = file.read()

        colors.pprint("cyan", "----------- START -----------")
        colors.pprint("reset", "{}".format(output))
        colors.pprint("cyan", "-------- END OF FILE --------")
        colors.pprint("reverse", "")
        input("Press a key to continue...")
        colors.pprint("reset", "\n")
        try:
            self.__close_and_encrypt(path_to_file)
        except:
            colors.pprint("red", "Error while closing and encrypting the file")
            raise
