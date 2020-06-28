#!/usr/bin/python3

from . import is_aion
from ._utils import no_aion


def add_entry(fname: str, package, entry_dict: dict = {}) -> None:
    """
    adds an new entry(s) to from argument 'language_locale' given language

    :param fname: str
        file name of the file you want to add the entry(s)
        language locale from the language to which the entry(s) is/are to be added
        syntax: <language locale>
        example: "de_DE"
    :param package: str
        package name to which the entry belongs
        syntax: "<package name>"
        example: "test_package"
    :param entry_dict: dict, optional
        all texts for execution of a function
        syntax: {<entry name>: <text of your entry>}
        example: {"test_entry": "Test function was executed correctly"}
    :return: None

    :since: 0.1.0
    """
    from os.path import isfile

    if isfile(fname) is False:
        raise FileNotFoundError("the file " + fname + " doesn't exist")

    from ._utils import BaseXMLWriter

    lng_adder = BaseXMLWriter(fname)
    for entry, text in entry_dict.items():
        if exist_entry(fname, package, entry) is True:
            raise IndexError("the entry " + entry + " already exist")
        lng_adder.add("<root>", package + "." + str(entry), text=str(text))
    lng_adder.write()


def create_lng_file(language_locale: str, extra_dict: dict = {}, **extra: str) -> None:
    """
    creates a new '.lng' file for given language locale with given entry_dict

    :param language_locale : str
        language locale of language from which the new file is to be created
        syntax: <language_locale>
        example: en_US
    :param extra_dict: dict, optional
        package name you want to add specific entries
        syntax: {<name of the package you want to add entries>: {{<name of the entry>: <text of the entry>}}
        example: {"test_package": {"test_entry": "This is the text for the test text entry"}}
    :param extra: kwargs, optional
        package name you want to add specific entries
        syntax: <name of the package you want to add entries>={<name of the entry>: <text of the entry>}
        example: test_package={"test_success": "The test was executed successfully", "text_error": "The test wasn't executed successfully"}
    :return: None

    :since: 0.1.0
    """
    from ._utils import BaseXMLBuilder
    from os import getcwd
    from os.path import isfile

    if isfile(getcwd() + "/" + language_locale + ".lng"):
        raise FileExistsError("the language file " + language_locale + ".lng already")

    lng_file = BaseXMLBuilder(language_locale)

    for package, entry_dict in extra_dict.items():
        for entry_name, entry_text in entry_dict.items():
            lng_file.create_root_element(language_locale, str(package) + "." + str(entry_name), text=str(entry_text))

    for package, entry_dict in extra.items():
        for entry_name, entry_text in entry_dict.items():
            lng_file.create_root_element(language_locale, str(package) + "." + str(entry_name), text=str(entry_text))
    lng_file.write(language_locale + ".lng")


def delete_entry(fname: str, package: str, entry_list: list = []) -> None:
    """
    deletes entries from '<language_locale>.lng'

    :param fname: str
        path to file you want to delete entries
        syntax: <fname>
        example: "en_US.lng"
    :param package: str
        name of the package from which the entries should be deleted
        syntax: <package name>
        example: "test"
    :param entry_list: list, optional
        name of the entries you want to remove
        syntax: [<entry name>]
        example: ["test_entry"]
    :return: None

    :since: 0.1.0
    """
    from ._utils import BaseXMLWriter

    lng_writer = BaseXMLWriter(fname)
    for item in entry_list:
        lng_writer.remove("language", str(package) + "." + str(item))


def exist_entry(fname: str, package: str, entry: str) -> bool:
    """
    checks if a entry exist

    :param fname: str
        file from which the entry should be search
        syntax: <language locale>
        example: "en_US"
    :param package: str
        package name from the entry
        syntax: <package name>
        example: "test"
    :param entry: str
        entry name of package (entry)
        syntax: <entry name>
        example: "test_entry"
    :return: bool
        returns True if entry exist / False if not
        syntax: <boolean>
        example: False

    :since: 0.1.0
    """
    from ._utils import BaseXMLReader

    entry = entry.replace(" ", "_")

    lng_reader = BaseXMLReader(fname)
    for item in lng_reader.get_infos(["<root>"]).items().index(0):
        if package + "." + entry in item["childs"]:
            return True
        else:
            return False


def start(skill: str, entry: str, format: dict = {}) -> str:
    """
    returns entry from given arguments

    :param skill: str
        name of the skill from the entry you want to call
        syntax: <skill name>
        example: "test_skill"
    :param entry: str
        name of the entry you want to call
        syntax: <entry>
        example: "test_func_entry"
    :param format: dict
        dictionary to format the string in the '.lng' file
        syntax: <format>
        example: {"test", "newtest"}: "This is a test" -> "This is a newtest"
    :return: str
        returns the (from 'format' formatted) string from the in '/etc/aion_data/config.xml' setted language locale '.lng' file
        syntax: <return string>
        example: "This is a test"

    :since: 0.1.0
    """
    if is_aion:
        from ._utils import import_aion_internal_file as _import_aion_internal_file
        return _import_aion_internal_file("language").start(skill=skill, entry=entry, format=format)
    else:
        no_aion()
