#! /usr/bin/env python3
# coding: utf-8


import os
import sh

# import required module
from cryptography.fernet import Fernet

class Encrypt:
    def __init__(self, file_to_encrypt):
        self.INPUT_FILE = file_to_encrypt

    def encrypt(self):
        file = self.INPUT_FILE
        print("file is ")
        print(file)

        print("Generating key")
        key = Fernet.generate_key()
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
        
        # opening the key
        print("Opening the key")
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
        
        print("Using the key")
        # using the generated key
        fernet = Fernet(key)
        
        # opening the original file to encrypt
        print("Opening the file")
        with open(file, 'rb') as file:
            original = file.read()

        print("Encrypting the file")            
        # encrypting the file
        encrypted = fernet.encrypt(original)
        
        # opening the file in write mode and 
        # writing the encrypted data
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print("Encryption completed")
    