#! /usr/bin/env python3
# coding: utf-8


from os import getenv
import sh

import settings.settings as cfg

# import required module
from cryptography.fernet import Fernet

class Decrypt:
    def __init__(self, file_to_decrypt):
        self.encrypted_file = file_to_decrypt
        self.home = getenv('HOME')
        self.config = cfg.Config(self.home)

    def get_key(self):

        key_directory = self.config.get_key_dir()
        key_filename = key_directory + self.encrypted_file + ".key"
        print("Opening the key")
        with open(key_filename, 'rb') as filekey:
            key = filekey.read()
        return key
        
    def decrypt_and_read(self):
        file_to_decrypt = self.encrypted_file
        # home = self.config.get_home_dir()
        workspace = self.config.get_workspace()
        path_to_file = workspace + file_to_decrypt

        print("Getting key")
        key = self.get_key()
        import pdb; pdb.set_trace()
        print("Using key")
        fernet = Fernet(key)

        print("Reading encrypted file")
        with open(path_to_file, 'rb') as encrypted_file:
            encrypted = encrypted_file.read()
        
        print("Decrypting the content")
        decrypted = fernet.decrypt(encrypted)

        print("Writing decrypted content")
        with open(path_to_file, 'wb') as decrypted_file:
            decrypted_file.write(decrypted)
        
        print("Displaying file content")
        with open(path_to_file, 'r') as file:
            output = file.read()
        
        print("----------- START -----------")
        print("{}".format(output))
        print("-------- END OF FILE --------")
        input("Press a key to close")
                
    