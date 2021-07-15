#! /usr/bin/env python3
# coding: utf-8

""" import required module """
import re
from os import getenv
from cryptography.fernet import Fernet
from settings import settings as cfg

class Encrypt:
    """ Encrypt"""
    def __init__(self, file_to_encrypt):
        self.file_to_encrypt = file_to_encrypt
        self.home = getenv('HOME')
        self.config = cfg.Config(self.home)

    @classmethod
    def __key_generator(cls, key_filename):
        """Generates"""
        
        print("Generating key")
        
        key = Fernet.generate_key()
        with open(key_filename, 'wb') as filekey:
            filekey.write(key)
        return key_filename

    @classmethod
    def __key_loader(self, key_filename):
        """ Generates """
        # opening the key
        print("Opening the key")
        with open(key_filename, 'rb') as filekey:
            key = filekey.read()
        return key

    def test_keygen(self):
        """Test Unit with pytest"""
        home = getenv("HOME")
        config = cfg.Config(home)
        dummy_file_path = home + config.CONFIG_DIR + "dummy.test"
        assert self.__key_generator(dummy_file_path)

    def test_keyloader(self):
        """Test Unit with pytest"""
        home = getenv("HOME")
        config = cfg.Config(home)
        dummy_file_path = home + config.CONFIG_DIR + "dummy.test.key"
        assert self.__key_loader(dummy_file_path)

    # def test_encrypt(self):
    #     assert self.encrypt()

    def encrypt(self):
        """Generates"""
        file = self.file_to_encrypt
        print("file is ")
        print(file)
        
        file_name = file.rsplit("/",1)[1]

        key_dir_path = self.config.get_key_dir()
        
        key_file = key_dir_path + file_name + ".key"
        key_gen = self.__key_generator(key_file)
        key = self.__key_loader(key_gen)
        print("Using the key")
        import pdb; pdb.set_trace()
        # using the generated key
        fernet = Fernet(key)

        # opening the original file to encrypt
        print("Opening the file")
        with open(file, 'rb') as origin_f:
            original = origin_f.read()

        print("Encrypting the file")
        # encrypting the file
        encrypted = fernet.encrypt(original)

        # opening the file in write mode and
        # writing the encrypted data
        with open(file, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
        print("Encryption completed")
