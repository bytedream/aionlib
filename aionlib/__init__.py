#!/usr/bin/python3

__author__ = "blueShard"
__license__ = "GPL-3.0"
__version__ = "0.1.0"

from ._utils import start_check as _start_check

_start_check()

is_aion = _start_check.is_aion
is_linux = _start_check.is_linux

from ._utils import aion_data_path, aion_path

from . import config, language, logging, plugin, utils, variable


def speech_output(speech_output: str) -> None:
    """
    plays a output of an artificial voice from the given words

    :param speech_output: str
        the words to be said
        syntax: <speech output words>
        example: "This is an test"
    :return: None

    :since: 0.1.0
    """
    if is_aion:
        from ._utils import import_aion_internal_file
        return import_aion_internal_file("__init__").speech_output(speech_output)
    else:
        from ._utils import no_aion
        no_aion()
