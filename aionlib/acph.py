#!/usr/bin/python3


def add_acph(fname: str, skill: str, acph_dict: dict = {}) -> None:
    """
    adds an new entry(s) to from argument 'language_locale' given language

    :param fname: str
        name of the file where the activate phrases should be added
        syntax: <file name>
        example: "/home/pi/test.acph"
    :param skill: str
        skill name to which the acph belongs
        syntax: "<skill name>"
        example: "test_skill"
    :param acph_dict: dict, optional
        defines a word or a sentence from which a method is called
        syntax: {<activate phrase>: <method that should get called after the activate phrase was said>}
        example: {"start test": "MyTestMethod"}
        NOTE: in key 'activate_phrase' you can use the '__and__' statement. This checks if the words before and after '__and__' are in the sentence that the user has spoken in

    :since: 0.1.0
    """
    try:
        from .utils import BaseXMLWriter
    except ImportError:
        from utils import BaseXMLWriter

    acph_writer = BaseXMLWriter(fname)
    for acph, method in acph_dict:
        if exist_acph(fname, acph):
            raise IndexError("the activate phrase " + acph + " already exist")
        acph_writer.add("<root>", acph, skill=skill, method=method)
    acph_writer.write()


def create_acph_file(language_locale: str, skill_acph_dict_dict: dict = {}) -> None:
    """
    creates a new '.acph' file for given language locale with given skill_acph_dict_dict

    :param language_locale: str
        language locale of language from which the new file is to be created
        syntax: <language_locale>
        example: "en_US"
    :param skill_acph_dict_dict: dict, optional
        skill name you want to add specific entries
        syntax: {<skill name>: {<activate phrase>: <method that should get called after the activate phrase was said>}}
        example: {"test_skill": {"start test": "MyTestMethod"}}
        NOTE: in key 'activate_phrase' you can use the '__and__' statement. This checks if the words before and after '__and__' are in the sentence that the user has spoken in
    :return: None

    :since: 0.1.0
    """
    try:
        from .utils import BaseXMLBuilder
    except ImportError:
        from utils import BaseXMLBuilder

    acph_builder = BaseXMLBuilder(language_locale)
    for skill, acph_dict in skill_acph_dict_dict.items():
        for acph, method in acph_dict.items():
            acph_builder.create_root_element(acph, skill=skill, method=method)

    acph_builder.write(language_locale + ".acph")


def delete_acph(fname: str, acph_list: list = []) -> None:
    """
    deletes entries from '<language_locale>.acph'

    :param fname: str
        file from which the activate phases is being deleted
        syntax: <language locale>
        example: "/home/pi/test.acph"
    :param acph_list: list, optional
        name of the activate phases you want to remove
        syntax: [<activate phase name>]
        example: ["test_acph"]
    :return: None

    :since: 0.1.0
    """
    try:
        from .utils import BaseXMLWriter
    except ImportError:
        from utils import BaseXMLWriter

    acph_writer = BaseXMLWriter(fname)
    for item in acph_list:
        acph_writer.remove("<root>", str(item))
    acph_writer.write()


def exist_acph(fname: str, acph: str) -> bool:
    """
    checks if a entry exist

    :param fname: str
        file from which the activate phrase should be search
        syntax: <language locale>
        example: "en_US"
    :param acph: str
        activate phrase you want to check if exists
        syntax: <acph name>
        example: "start test"
    :return: bool
        returns True if acph exist / False if not
        syntax: <boolean>
        example: False

    :since: 0.1.0
    """
    try:
        from .utils import BaseXMLReader
    except ImportError:
        from utils import BaseXMLReader

    acph = acph.replace(" ", "_")

    acph_reader = BaseXMLReader(fname)
    for item in acph_reader.get_infos(["<root>"]).items().index(0):
        if acph in item["childs"]:
            return True
        else:
            return False
