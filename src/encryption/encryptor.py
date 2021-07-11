#! /usr/bin/env python3
# coding: utf-8

""" import required module """
from cryptography.fernet import Fernet

class Encrypt:
    """ Encrypt"""
    def __init__(self, file_to_encrypt):
        self.INPUT_FILE = file_to_encrypt

    def key_generator(self, key_filename):
        """Generates"""
        print("Generating key")
        key = Fernet.generate_key()
        with open(key_filename, 'wb') as filekey:
            filekey.write(key)
        return filekey

    def key_reader(self, key_filename):
        """ Generates """
        # opening the key
        print("Opening the key")
        with open(key_filename, 'rb') as filekey:
            key = filekey.read()
        return key

    def encrypt(self):
        """Generates"""
        file = self.INPUT_FILE
        print("file is ")
        print(file)

        key_file = file + ".key"
        key_gen = key_generator(key_file)
        key = key_reader(key_gen)
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
