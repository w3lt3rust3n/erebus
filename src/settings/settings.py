#! /usr/bin/env python3
# coding: utf-8
"""Class for Erebus configuration"""
class Config:
    """All that we need to configure Erebus"""
    def __init__(self, user_home):
        self.home = user_home
        self.config_dir = user_home + "/.erebus/config/"
        self.workspace = user_home + "/erebus/files/"
        self.key_dir = user_home + "/.erebus/keys/"

    def get_conf_dir(self):
        """Return the path to the Erebus configuration directory."""
        return self.config_dir

    def get_workspace(self):
        """Return the path to Erebus workspace directory."""
        return self.workspace

    def get_key_dir(self):
        """Return the path to Erebus encrypted files keys directory."""
        return self.key_dir

    def get_home_dir(self):
        """Return the user home directory"""
        return self.home
