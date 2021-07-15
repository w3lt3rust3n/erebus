#! /usr/bin/env python3
# coding: utf-8
"""Class for Erebus configuration"""
class Config:
    """gngn"""
    def __init__(self, user_home):
        self.home = user_home
        self.config_dir = user_home + "/.erebus/config/"
        self.workspace = user_home + "/erebus/files/"
        self.key_dir = user_home + "/.erebus/keys/"

    def get_conf_dir(self):
        return self.config_dir

    def get_workspace(self):
        return self.workspace

    def get_key_dir(self):
        """gngng"""
        return self.key_dir

    def get_home_dir(self):
        """Return home directory"""
        return self.home
