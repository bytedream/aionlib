#!/usr/bin/python3

from . import aion_data_path as _aion_data_path


RUN_AFTER = "run_after"
RUN_BEFORE = "run_after"


run_after_path = _aion_data_path + "/plugins/run_after"
run_before_path = _aion_data_path + "/plugins/run_before"

run_after_file = _aion_data_path + "/plugins/run_after/run_after.xml"
run_before_file = _aion_data_path + "/plugins/run_before/run_before.xml"


class RunAfter:
    """
    base class to create custom 'run_after' plugins

    :since: 0.1.0
    """

    def __init__(self, activate_phrase: str, speech_input: str) -> None:
        """
        makes the variables available for all class functions

        :param activate_phrase: str
            activate phrase from which this class was called
            syntax: <activate phrase>
            example: "start plugin test"
        :param speech_input: str
            input that the user has spoken in
            syntax: <speech input>
            example: "start plugin test"
        :return: None

        :since: 0.1.0
        """
        self.activate_phrase = activate_phrase
        self.speech_input = speech_input

    def main(self) -> None:
        """
        gets called if the class get called from the 'run_after_plugin' plugin of the 'Skill' class

        :return: None

        :since: 0.1.0
        """
        pass


class RunBefore:
    """
    base class to create custom 'run_before' plugins

    :since: 0.1.0
    """

    def __init__(self, activate_phrase: str, speech_input: str) -> None:
        """
        makes the variables available for all class functions

        :param activate_phrase: str
            activate phrase from which this class was called
            syntax: <activate phrase>
            example: "start plugin test"
        :param speech_input: str
            input that the user has spoken in
            syntax: <speech input>
            example: "start plugin test"
        :return: None

        :since: 0.1.0
        """
        self.activate_phrase = activate_phrase
        self.speech_input = speech_input

    def main(self) -> None:
        """
        gets called if the class get called from the 'run_before_plugin' function of the 'Skill' class

        :return: None

        :since: 0.1.0
        """
        pass


def create_run_after_plugin_file(author: str,
                                 plugin_name: str,
                                 main_file: str,
                                 skill: str,
                                 plugin_methods: dict,
                                 version: str,
                                 additional_directories: list = [],
                                 description: str = "",
                                 language_locales: list = [],
                                 language_dict: dict = {},
                                 license: str = "",
                                 required_python3_packages: list = []) -> None:
    """
    creates a file from which a 'run_after' plugin can be installed

    :param author: str
        name of the author from the plugin
        syntax: <author name>
        example: "blueShard"
    :param main_file: str
        file name of file where all plugin methods are defined
        syntax: <file name>
        example: "test.py"
        NOTE: the file must be in the same directory as the file from which 'create_run_after_plugin_file' is being executed
    :param plugin_name: str
        root name of the plugin you create
        syntax: <plugin name>
        example: "text_plugin"
    :param skill: str
        name of the skill you want to add the 'run_before' plugin
        syntax: <skill name>
        example: "Play"
        NOTE: be case-sensitive!
    :param plugin_methods: dict
        dictionary of plugin pseudonym with plugin method you want to add to given 'skill'
        syntax: {"<plugin pseudonym>": <plugin methods>}
        example: ["test_plugin_run_test_2": "TestPlugin"]
        NOTE: be case-sensitive!
        NOTE2: the plugins pseudonyms are only pseudonyms for the given methods
        NOTE3: you can't remove individual plugins via the 'aion' command line command
    :param version: str
        version (number) of your plugin
        syntax: <version>
        example: "1.0.0"
    :param additional_directories: list, optional
        list of additional directories your main file needs for execution
        syntax: [<additional directories>]
        example: ["test_directory"]
        NOTE: the directories must be in the same directory as the file from which 'create_run_after_plugin_file' is being executed
    :param description: str, optional
        description of your plugin
        syntax: <description>
        example: "A simple plugin to test the method 'create_run_after_plugin_file'"
    :param language_locales: list
        list of language locales for which the 'language_dict' should be stored
        syntax: [<language locale>]
        example: ["en_US"]
    :param language_dict: dict, optional
        dictionary of messages which are saved in (from argument 'language_locales' given) '.lng' files
        syntax: {<entry>, <text>}
        example: {"test_entry": "The test was successful"}
        NOTE: the method name should be included in the entry for legibility
        NOTE2: for more infos about language ('.lng') files, see file 'language.py'
    :param license: str, optional
        license of the plugin
        syntax: <license>
        example: "MPL-2.0"
    :param required_python3_packages: list, optional
        list of python3 packages your plugin needs for correct execution
        syntax: [<python3 package>]
        example: ["aionlib"]
    :return: None

    :since: 0.1.0
    """
    _create_befater_plugin_file("run_after",
                                author,
                                plugin_name,
                                main_file,
                                skill,
                                plugin_methods,
                                version,
                                additional_directories,
                                description,
                                language_locales,
                                language_dict,
                                license,
                                required_python3_packages)


def create_run_before_plugin_file(author: str,
                                  plugin_name: str,
                                  main_file: str,
                                  skill: str,
                                  plugin_methods: dict,
                                  version: str,
                                  additional_directories: list = [],
                                  description: str = "",
                                  language_locales: list = [],
                                  language_dict: dict = {},
                                  license: str = "",
                                  required_python3_packages: list = []) -> None:
    """
    creates a file from which a 'run_before' plugin can be installed

    :param author: str
        name of the author from the plugin
        syntax: <author name>
        example: "blueShard"
    :param main_file: str
        file name of file where all plugin methods are defined
        syntax: <file name>
        example: "test.py"
        NOTE: the file must be in the same directory as the file from which 'create_run_before_plugin_file' is being executed
    :param plugin_name: str
        root name of the plugins you create
        syntax: <plugin name>
        example: "text_plugin"
    :param skill: str
        name of the skill you want to add the 'run_before' plugin
        syntax: <skill name>
        example: "Play"
        NOTE: be case-sensitive!
    :param plugin_methods: dict
        dictionary of plugin pseudonym with plugin method you want to add to given 'skill'
        syntax: {"<plugin pseudonyms>": <plugin methods>}
        example: ["test_plugin_run_test_2": "TestPlugin"]
        NOTE: be case-sensitive!
        NOTE2: the plugins pseudonyms are only pseudonyms for the given methods
        NOTE3: you can't remove individual plugins via the 'aion' command line command
    :param plugin_name: str
        name of the plugin you create
        syntax: <plugin name>
        example: "text_plugin"
    :param version: str
        version (number) of your plugin
        syntax: <version>
        example: "1.0.0"
    :param additional_directories: list, optional
        list of additional directories your main file needs for execution
        syntax: [<additional directories>]
        example: ["test_directory"]
        NOTE: the directories must be in the same directory as the file from which 'create_run_before_plugin_file' is being executed
    :param description: str, optional
        description of your plugin
        syntax: <description>
        example: "A simple plugin to test the method 'create_run_after_plugin_file'"
    :param language_locales: list
        list of language locales for which the 'language_dict' should be stored
        syntax: [<language locale>]
        example: ["en_US"]
    :param language_dict: dict, optional
        dictionary of messages which are saved in (from argument 'language_locales' given) '.lng' files
        syntax: {<entry>, <text>}
        example: {"test_entry": "The test was successful"}
        NOTE: the method name should be included in the entry for legibility
        NOTE2: for more infos about language ('.lng') files, see file 'language.py'
    :param license: str, optional
        license of the plugin
        syntax: <license>
        example: "MPL-2.0"
    :param required_python3_packages: list, optional
        list of python3 packages your plugin needs for correct execution
        syntax: [<python3 package>]
        example: ["aionlib"]
    :return: None

    :since: 0.1.0
    """
    _create_befater_plugin_file("run_before",
                                author,
                                plugin_name,
                                main_file,
                                skill,
                                plugin_methods,
                                version,
                                additional_directories,
                                description,
                                language_locales,
                                language_dict,
                                license,
                                required_python3_packages)


def create_plugin_package(dir_name: str) -> None:
    """
    creates a stand alone file ('.plugin') from given directory

    :param dir_name : str
        directory name of the directory from which you want to create a '.plugin' file
        syntax: <directory name>
        example: "/home/pi/test/"
    :return: None

    :note: 'plugin.aion' file must be in the given directory (see 'create_run_after_plugin_file' / 'create_run_before_plugin_file' to create a 'plugin.aion' file)

    :since: 0.1.0
    """
    from os import listdir, mkdir, rename
    from os.path import isdir
    from random import sample
    from shutil import make_archive, rmtree

    if isdir(dir_name) is False:
        raise NotADirectoryError("couldn't find the directory '" + dir_name + "'")

    name = ""
    file_num = 0
    for file in listdir(dir_name):
        if file.endswith(".aion"):
            file_num += 1
            name = "".join(file.split(".aion")[0])
    if file_num == 0:
        raise FileNotFoundError("couldn't find .aion file in " + dir_name + ". To create one use the 'create_plugin_file' function in aionlib.skill")
    elif file_num > 1:
        raise FileExistsError("expected one .aion file in " + dir_name + ", got " + str(file_num))

    plugin_dir_name = "plugin_" + name + "".join([str(num) for num in sample(range(1, 10), 5)])
    mkdir(plugin_dir_name)

    make_archive(name + ".plugin", "zip", plugin_dir_name)
    rename(plugin_dir_name + ".plugin.zip", plugin_dir_name + ".plugin")

    rmtree(plugin_dir_name)


def get_all_run_after_plugins() -> dict:
    """
    get all installed 'run_after' plugins + infos

    :return: dict
        returns dict of all plugins + infos

    :since: 0.1.0
    """
    from . import is_aion
    from .utils import is_dict_in_dict
    from ._utils import no_aion, BaseXMLReader

    run_after = {}

    if is_aion:
        for value in BaseXMLReader(run_after_file).get_infos("<all>").values():
            for child in value:
                attrib = child["attrib"]
                parent_tag = child["parent"]["tag"]
                parent_attrib = child["parent"]["attrib"]
                if is_dict_in_dict({"type": "skill"}, parent_attrib):
                    try:
                        run_after[parent_tag][child["tag"]] = {"method": attrib["method"], "root_plugin": attrib["root_plugin"]}
                    except KeyError:
                        run_after[parent_tag] = {}
                else:
                    for skill in run_after.values():
                        for plugin in skill:
                            if plugin == parent_tag:
                                run_after[skill][plugin][child["tag"]] = child["text"]
                                break
    else:
        no_aion()

    return run_after


def get_all_run_before_plugins() -> dict:
    """
    get all installed 'run_before' plugins + infos

    :return: dict
        returns dict of all plugins + infos

    :since: 0.1.0
    """
    from . import is_aion
    from .utils import is_dict_in_dict
    from ._utils import no_aion, BaseXMLReader

    run_before = {}

    if is_aion:
        for value in BaseXMLReader(run_before_file).get_infos("<all>").values():
            for child in value:
                attrib = child["attrib"]
                parent_tag = child["parent"]["tag"]
                parent_attrib = child["parent"]["attrib"]
                if is_dict_in_dict({"type": "skill"}, parent_attrib):
                    try:
                        run_before[parent_tag][child["tag"]] = {"method": attrib["method"], "root_plugin": attrib["root_plugin"]}
                    except KeyError:
                        run_before[parent_tag] = {}
                else:
                    for skill in run_before.values():
                        for plugin in skill:
                            if plugin == parent_tag:
                                run_before[skill][plugin][child["tag"]] = child["text"]
                                break
    else:
        no_aion()

    return run_before


def get_run_after_plugin_infos(plugin_name: str) -> dict:
    """
    returns infos about an given 'run_after' plugin

    :param plugin_name: str
        the name of the 'run_after' plugin
        syntax: <plugin name>
        example: "test_plugin"
    :return: dict
        returns a dictionary with infos of the 'run_after' plugin
        syntax: {"author": <author>,
                "main_file": <main file>,
                "plugin_root_name": <plugin root name>
                "plugin_name": <plugin name>,
                "plugin_method": <plugin method>
                "version": <version>,
                "additional_directories": [<additional directories>],
                "description": <description>,
                "language_locales": [<language locales>],
                "language_dict": {<entry>: <text>}
                "license": <license>,
                "required_python3_packages": [<python3 packages>]}
        example: {"author": "blueShard",
                "main_file": "test.py",
                "plugin_root_name:": "test_plugin"
                "plugin_name": "test_plugin_run_after",
                "plugin_method": "test_plugin_method"
                "version": "1.0.0",
                "additional_directories": ["test_directory"],
                "description": "A simple plugin to test the method 'get_run_after_plugin_infos",
                "language_locales": ["en_US"],
                "language_dict": {"test_method": "The test was successful"},
                "license": "MPL-2.0",
                "required_python3_packages": ["aionlib"]}

    :since: 0.1.0
    """
    for skill in get_all_run_after_plugins().values():
        for plugin, infos in skill.values():
            if plugin == plugin_name:
                return infos


def get_run_before_plugin_infos(plugin_name: str) -> dict:
    """
    returns infos about an given 'run_before' plugin

    :param plugin_name: str
        the name of the 'run_after' plugin
        syntax: <plugin name>
        example: "test_plugin"
    :return: dict
        returns a dictionary with infos of the 'run_after' plugin
        syntax: {"author": <author>,
                "main_file": <main file>,
                "plugin_root_name": <plugin root name>
                "plugin_name": <plugin name>,
                "plugin_method": <plugin method>
                "version": <version>,
                "additional_directories": [<additional directories>],
                "description": <description>,
                "language_locales": [<language locales>],
                "language_dict": {<entry>: <text>}
                "license": <license>,
                "required_python3_packages": [<python3 packages>]}
        example: {"author": "blueShard",
                "main_file": "test.py",
                "plugin_root_name:": "test_plugin"
                "plugin_name": "test_plugin_run_before",
                "plugin_method": "test_plugin_method"
                "version": "1.0.0",
                "additional_directories": ["test_directory"],
                "description": "A simple plugin to test the method 'get_run_before_plugin_infos",
                "language_locales": ["en_US"],
                "language_dict": {"test_method": "The test was successful"},
                "license": "MPL-2.0",
                "required_python3_packages": ["aionlib"]}

    :since: 0.1.0
    """
    for skill in get_all_run_before_plugins().values():
        for plugin, infos in skill.values():
            if plugin == plugin_name:
                return infos


def _create_befater_plugin_file(type: (RUN_AFTER, RUN_BEFORE),
                                author: str,
                                plugin_name: str,
                                main_file: str,
                                skill: str,
                                plugin_methods: dict,
                                version: str,
                                additional_directories: list = [],
                                description: str = "",
                                language_locales: list = [],
                                language_dict: dict = {},
                                license: str = "",
                                required_python3_packages: list = []) -> None:
    """
    creates a file from which a plugin can be installed

    :param type: (RUN_AFTER, RUN_BEFORE)
        type of the plugin
        syntax: <plugin type>
        example: RUN_AFTER
    :param author: str
        name of the author from the plugin
        syntax: <author name>
        example: "blueShard"
    :param main_file: str
        file name of file where all plugin methods are defined
        syntax: <file name>
        example: "test.py"
        NOTE: the file must be in the same directory as the file from which 'create_run_after_plugin_file' is being executed
    :param plugin_name: str
        root name of the plugin you create
        syntax: <plugin name>
        example: "text_plugin"
    :param skill: str
        name of the skill you want to add the 'run_before' plugin
        syntax: <skill name>
        example: "Play"
        NOTE: be case-sensitive!
    :param plugin_methods: dict
        dictionary of plugin pseudonym with plugin method you want to add to given 'skill'
        syntax: {"<plugin pseudonym>": <plugin methods>}
        example: ["test_plugin_run_test_2": "TestPlugin"]
        NOTE: be case-sensitive!
        NOTE2: the plugins pseudonyms are only pseudonyms for the given methods
        NOTE3: you can't remove individual plugins via the 'aion' command line command
    :param version: str
        version (number) of your plugin
        syntax: <version>
        example: "1.0.0"
    :param additional_directories: list, optional
        list of additional directories your main file needs for execution
        syntax: [<additional directories>]
        example: ["test_directory"]
        NOTE: the directories must be in the same directory as the file from which 'create_run_after_plugin_file' is being executed
    :param description: str, optional
        description of your plugin
        syntax: <description>
        example: "A simple plugin to test the method 'create_run_after_plugin_file'"
    :param language_locales: list
        list of language locales for which the 'language_dict' should be stored
        syntax: [<language locale>]
        example: ["en_US"]
    :param language_dict: dict, optional
        dictionary of messages which are saved in (from argument 'language_locales' given) '.lng' files
        syntax: {<entry>, <text>}
        example: {"test_entry": "The test was successful"}
        NOTE: the method name should be included in the entry for legibility
        NOTE2: for more infos about language ('.lng') files, see file 'language.py'
    :param license: str, optional
        license of the plugin
        syntax: <license>
        example: "MPL-2.0"
    :param required_python3_packages: list, optional
        list of python3 packages your plugin needs for correct execution
        syntax: [<python3 package>]
        example: ["aionlib"]
    :return: None

    :since: 0.1.0
    """
    from os import getcwd, listdir

    write_dict = {}

    if isinstance(author, str) is False:
        raise TypeError("argument 'author' must be str, got " + type(author).__name__)
    write_dict["author"] = author

    if isinstance(main_file, str) is False:
        raise TypeError("argument 'main_file' must be str, got " + type(author).__name__)
    if main_file not in listdir(getcwd()):
        raise FileNotFoundError("couldn't find the file " + main_file + " in current directory")
    if main_file[:-3] == plugin_name is False:
        raise NameError("the file name from " + main_file + " must be same as the argument 'name' (" + plugin_name + ")")
    if main_file not in listdir(getcwd()):
        raise FileNotFoundError("couldn't find the file '" + main_file + "' in current directory")
    write_dict["main_file"] = main_file

    if isinstance(plugin_name, str) is False:
        raise TypeError("argument 'plugin_name' must be str, got " + type(plugin_name).__name__)
    write_dict["plugin_name"] = plugin_name

    if isinstance(skill, str) is False:
        raise TypeError("argument 'plugin_name' must be dict, got " + type(plugin_methods).__name__)
    write_dict["skill"] = skill

    if isinstance(plugin_methods, dict) is False:
        raise TypeError("argument 'plugin_name' must be dict, got " + type(plugin_methods).__name__)
    write_dict["plugin_methods"] = plugin_methods

    if isinstance(version, str) is False:
        raise TypeError("argument 'version' must be str, got " + type(version).__name__)
    write_dict["version"] = version

    # ----- #

    if isinstance(additional_directories, (list, tuple)) is False:
        raise TypeError("argument 'additional_directories' must be list or tuple, got " + type(additional_directories).__name__)
    for directory in additional_directories:
        if directory not in listdir(getcwd()):
            raise NotADirectoryError("couldn't find the directory " + directory + " in current directory")
    write_dict["additional_directories"] = additional_directories

    if isinstance(description, str) is False:
        raise TypeError("argument 'description' must be str, got " + type(description).__name__)
    write_dict["description"] = description

    if isinstance(language_locales, (list, tuple)) is False:
        raise TypeError("argument 'language_locales' must be list or tuple, got " + type(language_locales).__name__)
    write_dict["language_locales"] = language_locales

    if isinstance(language_dict, dict) is False:
        raise TypeError("argument 'language_success' must be dict, got " + type(language_dict).__name__)
    for key in language_dict.keys():
        tmp_string = ""
        for char in key:
            if char == " ":
                char = "_"
            if char.lower() not in "abcdefghijklmnopqrstuvwxyz_":
                raise ValueError("letter " + str(char) + " in " + str(key) + " must be in 'ABCDEFGHIJLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz_'")
            tmp_string = tmp_string + char
        language_dict[tmp_string] = language_dict.pop(key)
    write_dict["language_dict"] = language_dict

    if isinstance(license, str) is False:
        raise TypeError("argument 'license' must be str, got " + type(license).__name__)
    write_dict["license"] = license

    if isinstance(required_python3_packages, (list, tuple)) is False:
        raise TypeError("argument 'required_python3_packages' must be list or tuple, got " + type(required_python3_packages).__name__)
    write_dict["required_python3_packages"] = required_python3_packages

    # ----- #

    with open("plugin.aion", "w") as file:
        file.write("#type: " + type.lower() + "_plugin\n")
        for key, value in write_dict.items():
            file.write(key + " = " + str(value) + "\n")
        file.close()


def _run_befater_plugin(type: str, fname: str, plugin_name: str, activate_phrase: str, speech_input: str) -> None:
    """
    runs a plugin

    :param type: (RUN_AFTER, RUN_BEFORE)
        type of the plugin
        syntax: <plugin type>
        example: RUN_AFTER
    :param fname: str
        file path of the plugin file
        syntax: <filename>
        example: "/home/pi/test.py"
    :param plugin_name: str
        name of the plugin
        syntax: <plugin name>
        example: "TestPlugin"
    :param activate_phrase: str
        activate phrase, which calls the skill class to which the plugin belongs
        syntax: <activate phrase>
        example: "Start test plugin"
    :param speech_input: str
        speech input, which calls the skill class to which the plugin belongs
        syntax: <speech input>
        example: "Start test plugin"
    :return: None

    :since: 0.1.0
    """
    from sys import path
    path.insert(1, _aion_data_path + "/" + type.lower())
    exec("__import__('" + fname + "')." + plugin_name + "(" + activate_phrase + ", " + speech_input + ").main()")