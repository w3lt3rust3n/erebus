#! /usr/bin/env python3
# coding: utf-8

class Config:
    def __init__(self, user_home):
        self.CONFIG_DIR = user_home + "/.erebus/config/"
        self.WORKSPACE = user_home + "/erebus/files/"

    def __get_conf_dir(self):
        return self.CONFIG_DIR

    def __get_workspace(self):
        return self.WORKSPACE

