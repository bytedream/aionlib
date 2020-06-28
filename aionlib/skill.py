#!/usr/bin/python3

from . import aion_data_path as _aion_data_path


skills_path = _aion_data_path + "/skills"
skills_file = skills_path + "/skills.xml"


class Skill:
    """
    base class for use custom skills

    :since: 0.1.0
    """

    def __init__(self, activate_phrase: str, speech_input: str, run_after_plugins: dict, run_before_plugins: dict) -> None:
        """
        :param activate_phrase: str
            activate phrase that called this class
            syntax: "<activate phrase>"
            example: "test"
        :param speech_input: str
            complete spoken words
            syntax: "<speech input>"
            example: "Start the test"
        :param run_after_plugins: dict
            all run after plugins
        :param run_before_plugins: dict
            all run before plugins
        :return: None

        :since: 0.1.0
        """
        self.activate_phrase = activate_phrase
        self.activate_phrase_list = activate_phrase.split("__and__")
        self.speech_input = speech_input

        try:
            self.run_after_plugins = run_after_plugins[self.__class__.__name__]
        except KeyError:
            self.run_after_plugins = {}
        try:
            self.run_before_plugins = run_before_plugins[self.__class__.__name__]
        except KeyError:
            self.run_before_plugins = {}

    def main(self) -> None:
        """
        gets called if user says the defined activate_phrase

        :return: None

        :since: 0.1.0
        """
        pass

    def run_after(self) -> None:
        """
        gets called after the 'main' function was executed

        :return: None

        :since: 0.1.0
        """
        pass

    def run_before(self) -> None:
        """
        gets called before the 'main' function was executed

        :return: None

        :since: 0.1.0
        """
        pass

    def start_run_after_plugin(self, plugin_name: str) -> None:
        """
        calls a 'run_after' plugin (all plugins are in at the root of 'run_after_plugins' dict)

        :param plugin_name: str
            name of the plugin that should called (all plugins are in at the root of 'run_after_plugins' dict)
            syntax: "<plugin name>"
            example: "ExampleClass
        :return: None

        :since: 0.1.0
        """
        try:
            from .plugin import _run_befater_plugin, RUN_AFTER
        except ImportError:
            from plugin import _run_befater_plugin, RUN_AFTER

        if plugin_name in self.run_after_plugins:
            _run_befater_plugin(RUN_AFTER, plugin_name, self.run_after_plugins[plugin_name]["method"], self.activate_phrase, self.speech_input)

    def start_run_before_plugin(self, plugin_name: str) -> None:
        """
        calls a 'run_before' plugin (all plugins are in at the root of 'run_before_plugins' dict)

        :param plugin_name: str
            name of the plugin that should called (all plugins are in at the root of 'run_before_plugins' dict)
            syntax: <plugin name>
            example: "ExampleClass"
        :return: None

        :since: 0.1.0
        """
        try:
            from .plugin import _run_befater_plugin, RUN_BEFORE
        except ImportError:
            from plugin import _run_befater_plugin, RUN_BEFORE

        if plugin_name in self.run_before_plugins:
            _run_befater_plugin(RUN_BEFORE, plugin_name, self.run_before_plugins[plugin_name]["method"], self.activate_phrase, self.speech_input)

    def speech_output(self, speech_output: str) -> None:
        """
        plays a output of an artificial voice from the given words

        :param speech_output: str
            the words to be said
            syntax: <speech output words>
            example: "This is an test"
        :return: None

        :since: 0.1.0
        """
        try:
            from . import speech_output as _speech_output
        except ImportError:
            from .__init__ import speech_output as _speech_output

        _speech_output(speech_output)


def create_skill_file(activate_phrases: dict,
                      author: str,
                      language_locales: list,
                      main_file: str,
                      skill_name: str,
                      version: str,
                      additional_directories: list = [],
                      description: str = "",
                      language_dict: dict = {},
                      license: str = "",
                      required_python3_packages: list = []) -> None:
    """
    creates a file from which a skill can be installed

    :param activate_phrases: dict
        defines a word or a sentence from which a method is called
        syntax: {<activate phrase>: <method that should get called after the activate phrase was said>}
        example: {"start test": "MyTestMethod"}
        NOTE: in key 'activate_phrase' you can use the '__and__' statement. This checks if the words before and after '__and__' are in the sentence that the user has spoken in
    :param author: str
        name of the author from the skill
        syntax: <author name>
        example: "blueShard"
    :param language_locales: list
        list of language locales for which the skill is available
        syntax: [<language locale>]
        example: ["en_US"]
    :param main_file: str
        file name of file where all methods for the activate_phrases are defined
        syntax: <file name>
        example: "test.py"
        NOTE: the file must be in the same directory as the file from which 'create_skill_file' is being executed
    :param skill_name: str
        name of the skill you create
        syntax: <skill name>
        example: "text_skill"
    :param version: str
        version (number) of your skill
        syntax: <version>
        example: "1.0.0"

    :param additional_directories: list, optional
        list of additional directories your main file needs for execution
        syntax: [<additional directories>]
        example: ["test_directory"]
        NOTE: the directories must be in the same directory as the file from which 'create_skill_file' is being executed
    :param description: str, optional
        description of your skill
        syntax: <description>
        example: "A simple skill to test the method 'create_skill_file'"
    :param language_dict: dict, optional
        dictionary of messages which are saved in (from argument 'language_locales' given) '.lng' files
        syntax: {<entry>, <text>}
        example: {"test_entry": "The test was successful"}
        NOTE: the method name should be included in the entry for legibility
        NOTE2: for more infos about language ('.lng') files, see file 'language.py'
    :param license: str, optional
        license of the skill
        syntax: <license>
        example: "MPL-2.0"
    :param required_python3_packages: list, optional
        list of python3 packages your package needs for correct execution
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

    if isinstance(language_locales, (list, tuple)) is False:
        raise TypeError("argument 'language_locales' must be list or tuple, got " + type(language_locales).__name__)
    write_dict["language_locales"] = language_locales

    if isinstance(main_file, str) is False:
        raise TypeError("argument 'main_file' must be str, got " + type(author).__name__)
    if main_file not in listdir(getcwd()):
        raise FileNotFoundError("couldn't find the file " + main_file + " in current directory")
    if main_file[:-3] == skill_name is False:
        raise NameError("the file name from " + main_file + " must be same as the argument 'name' (" + skill_name + ")")
    if main_file not in listdir(getcwd()):
        raise FileNotFoundError("couldn't find the file '" + main_file + "' in current directory")
    write_dict["main_file"] = main_file

    if isinstance(skill_name, str) is False:
        raise TypeError("argument 'skill_name' must be str, got " + type(skill_name).__name__)
    write_dict["pskill_name"] = skill_name

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

    if isinstance(activate_phrases, dict) is False:
        raise TypeError("argument 'activate_phrases' must be dict, got " + type(activate_phrases).__name__)
    for item in activate_phrases:
        tmp_string = ""

        for char in item:
            if char == " ":
                char = "_"
            if char.lower() not in "abcdefghijklmnopqrstuvwxyz-_":
                raise ValueError("letter " + str(char) + " in " + str(item) + " must be in 'ABCDEFGHIJLMNOPQRSTUVWXYZabcdefghijklmopqrstuvwxyz-_'")
            tmp_string = tmp_string + char
        activate_phrases[tmp_string] = activate_phrases.pop(item)
    write_dict["activate_phrases"] = activate_phrases

    # ----- #

    with open("skill.aion", "w") as file:
        file.write("#type: skill\n")
        for key, value in write_dict.items():
            file.write(key + " = " + str(value) + "\n")
        file.close()


def get_all_skills() -> list:
    """
    returns all installed skills

    :return: list
        returns list of all installed skills
        syntax: [<skill>]
        example: ["skills"]
    :return: None

    :since: 0.1.0
    """
    from . import is_aion
    from ._utils import no_aion, BaseXMLReader

    if is_aion:
        return BaseXMLReader(skills_file).get_infos("<root>").items().index(0)[0]["childs"]
    else:
        no_aion()
        return []


def get_skill_infos(skill_name: str) -> dict:
    """
    returns infos about an given skill

    :param skill_name: str
        name of the skill you want to get infos about
        syntax: <skill name>
        example: "test_skill"
    :return: dict
        returns a dictionary with infos of the skill
        syntax: {"activate_phrases": {<activate phrases>},
                "author": <author>,
                "language_locales": [<language locales>],
                "main_file": <main file>,
                "skill_name": <skill name>,
                "version": <version>,
                "additional_directories": [<additional directories>],
                "description": <description>,
                "language_dict": {<entry>: <text>}
                "license": <license>,
                "required_python3_packages": [<python3 packages>]}
        example: {"activate_phrases": {"start test": "test_method_start"}},
                "author": "blueShard",
                "language_locales": ["en_US"],
                "main_file": "test.py",
                "skill_name": "text_skill",
                "version": "1.0.0",
                "additional_directories": ["test_directory"],
                "description": "A simple skill to test the function 'get_skill_infos",
                "language_dict": {"test_func": "The test was successful"},
                "license": "MPL-2.0",
                "required_python3_packages": ["aionlib"]}

    :since: 0.1.0
    """
    from . import is_aion
    from ._utils import no_aion, BaseXMLReader

    if is_aion:
        from ast import literal_eval
        skill_reader = BaseXMLReader(skills_file)
        return_dict = {"skill_name": skill_name}
        for value_list in skill_reader.get_infos("<all>").values():
            for skill in value_list:
                try:
                    if skill["parent"]["tag"] == skill_name:
                        try:
                            return_dict[skill["tag"]] = literal_eval(skill["text"])
                        except (EOFError, SyntaxError, ValueError):
                            return_dict[skill["tag"]] = skill["text"]
                except KeyError:
                    pass
        return return_dict

    else:
        no_aion()
        return {}
