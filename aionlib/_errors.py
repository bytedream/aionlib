#!/usr/bin/python3


class AionNotInstalledError(Exception):

    def __init__(self):
        super().__init__("Aion isn't installed")