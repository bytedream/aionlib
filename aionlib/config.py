#!/usr/bin/python3

from . import is_aion
from ._utils import no_aion

if is_aion:
    from ._utils import import_aion_internal_file as _import_aion_internal_files
    _config = _import_aion_internal_files("config")


class Aion:

    def __init__(self) -> None:
        if is_aion:
            self._aion_config = _config.Aion()

        self.all_listening_modes = ["auto", "manual"]
        self.all_stt_engines = ["google", "pocketsphinx"]
        self.all_time_formats = ["12", "24"]
        self.all_tts_engines = ["pico2wave", "espeak"]
        self.supported_languages = ["de_DE", "en_US"]

    def get_hotword_file(self) -> str:
        """
        get set hotword file path

        :return: str
            returns path of the hotword file
            syntax: <hotword file path>
            example: "/usr/local/aion-<aion_version>/etc/Aion.pmdl"

        :since: 0.1.0
        """
        if is_aion:
            return self._aion_config.get_hotword_file()
        else:
            no_aion()

    def get_language(self) -> str:
        """
        get sett language locale

        :return: str
            returns language locale
            syntax: <language locale>
            example: "en_US"

        :since: 0.1.0
        """
        if is_aion:
            return self._aion_config.get_language()
        else:
            no_aion()

    def get_listening_mode(self) -> str:
        """
        get set listening mode

        :return: str
            returns listening mode
            syntax: <listening mode>
            example: "auto"

        :since: 0.1.0
        """
        if is_aion:
            return self._aion_config.get_listening_mode()
        else:
            no_aion()

    def get_pid_manipulation_number(self) -> int:
        """
        get set pid manipulation number

        :return: int
            returns the pid manipulation number
            syntax: <pid manipulation number>
            example: 4

        :since: 0.1.0
        """
        if is_aion:
            return int(self._aion_config.get_pid_manipulation_number())
        else:
            no_aion()

    def get_stt_engine(self) -> str:
        """
        get set speech-to-text engine

        :return: str
            returns speech-to-text engine
            syntax: <speech-to-text engine>
            example: "google"

        :since: 0.1.0
        """
        if is_aion:
            return self._aion_config.get_stt_engine()
        else:
            no_aion()

    def get_time_format(self) -> int:
        """
        get set time format

        :return: str
            returns time format
            syntax: <time format>
            example: 24
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            return int(self._aion_config.get_time_format())
        else:
            no_aion()

    def get_tts_engine(self) -> str:
        """
        get set text-to-speech engine

        :return: str
            returns text-to-speech engine
            syntax: <text-to-speech engine>
            example: "espeak"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            return self._aion_config.get_tts_engine()
        else:
            no_aion()

    def set_hotword_file(self, hotword_file: str) -> None:
        """
        sets the hotword file

        :param hotword_file: str
            location from the new hotword file
            syntax: <hotword_file>
           example: "/usr/local/aion-*/etc/Aion.pmdl"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_hotword_file(hotword_file)
        else:
            no_aion()

    def set_language(self, language: str) -> None:
        """
        sets the language locale

        :param language: str
            new language locale
            syntax: <language locale>
            example: "en_US"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_language(language)
        else:
            no_aion()

    def set_listening_mode(self, listening_mode: str) -> None:
        """
        sets the listening mode

        :param listening_mode: str
            new listening mode
            syntax: <listening mode>
            example: "auto"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_listening_mode(listening_mode)
        else:
            no_aion()

    def set_pid_manipulation_number(self, pid_manipulation_number: int) -> None:
        """
        sets the pid manipulation number

        :param pid_manipulation_number: int
            new pid manipulation number
            syntax: <pid manipulation number>
            example: 4
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_pid_manipulation_number(pid_manipulation_number)
        else:
            no_aion()

    def set_stt_engine(self, stt_engine: str) -> None:
        """
        sets the spech-to-text engine

        :param stt_engine : str
            new speech-to-text engine
            syntax: <speech-to-text engine>
            example: "google"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_stt_engine(stt_engine)
        else:
            no_aion()

    def set_time_format(self, time_format: str) -> None:
        """
        sets the time format

        :param time_format: str
            new time format
            syntax: <time format>
            example: "24"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_time_format(time_format)
        else:
            no_aion()

    def set_tts_engine(self, tts_engine: str) -> None:
        """
        sets the text-to-speech engine

        :param tts_engine: str
            new text-to-speech engine
            syntax: <text-to-speech engine>
            example: "espeak"
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_config.set_tts_engine(tts_engine)
        else:
            no_aion()


def add_entry(name: str, text: str = None, attrib: dict = {}, parent_name: str = "config", parent_attrib: dict = {}) -> None:
    """
    adds an entry from the config file

    :param name: str
        name of the new entry
        syntax: <name>
        example: "test_entry"
    :param text: str, optional
        text of the new entry
        syntax: <text>
        example: "Test"
    :param attrib: dict, optional
        attributes of the new entry
        syntax: {<attribute name>: <attribute value>}
        example: {"test_attrib", "test"}
    :param parent_name: str, optional
        name of the parent entry to which the entry is added
        syntax: <parent name>
        example: "test_parent"
    :param parent_attrib: dict, optional
        attributes of the parent entry
        syntax: {<parent attribute name>: <parent attribute value>}
        example: {"version": "1.0.0"}
    :return: None

    :since: 0.1.0
    """
    if is_aion:
        _config.add_entry(name=name, text=text, attrib=attrib, parent_name=parent_name, parent_attrib=parent_attrib)
    else:
        no_aion()


def delete_entry(name: str, parent_name: str = "config", parent_attrib: dict = {}) -> None:
    """
    deletes an entry from the config file

    :param name: str
        name of the entry to be deleted
        syntax: <name>
        example: "test_entry"
    :param parent_name: str, optional
        name of the parent entry of the entry to be deleted
        syntax: <parent name>
        example: "test_parent"
    :param parent_attrib: dict, optional
        attributes of the parent entry from the entry to be searched
        syntax: {<attribute name>: <attribute value>}
        example: {"test_attrib", "test"}
    :return: None

    :since: 0.1.0
    """
    if is_aion:
        _config.delete_entry(name=name, parent_name=parent_name, parent_attrib=parent_attrib)
    else:
        no_aion()


def get_entry(name: str, parent_name: str = None, parent_attrib: dict = {}) -> None:
    """
    get infos about an entry

    :param name: str
        name of the entry to be searched
        syntax: <name>
        example: "test_entry"
    :param parent_name: str, optional
        name of the parent entry of the entry to be deleted
        syntax: <parent name>
        example: "test_parent"
    :param parent_attrib: dict, optional
        attributes of the parent entry
        syntax: {<attribute name>: <attribute value>}
        example: {"test_attrib", "test"}
    :return: dict
        returns the infos about the given entry
        syntax: {"text": <text of entry>, "attrib": <attributes of entry>}
        e.g.: {"text": "entry text", "attrib": {"version": "1.0.0"}}

    :since: 0.1.0
    """
    if is_aion:
        return _config.get_entry(name=name, parent_name=parent_name, parent_attrib=parent_attrib)
    else:
        no_aion()


def update_entry(name: str, text: str = None, attrib: dict = {}, parent_name: str = "config", **extra: str) -> None:
    """
    updates an entry

    :param name: str
        name of the entry to be updated
        syntax: <name>
        example: "test_entry"
    :param text: str, optional
        new text of the entry to be updated
        syntax: <text>
        example: "new test text"
    :param attrib: dict, optional
        new attributes of the entry to be updated
        syntax: {<attribute name>: <attribute value>}
        example: {"new_test_attrib", "new_test"}
    :param parent_name: str, optional
        parent entry of the entry to be updated
        syntax: <parent name>
        example: "test_parent"
    :return: None

    :since: 0.1.0
    """
    if is_aion:
        _config.update_entry(name=name, text=text, attrib=attrib.update(extra), parent_name=parent_name)
    else:
        no_aion()
