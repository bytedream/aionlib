#!/usr/bin/python3

from glob import glob as _glob

from xml.dom import minidom as _minidom
import xml.etree.ElementTree as _ET


aion_data_path = "/etc/aion_data"
aion_path = "".join(_glob("/usr/local/aion-*"))


def import_aion_internal_file(fname: str):
    """
    imports an file from the aion core

    :param fname: str
        name of the file
        syntax: <filename>
        example: "version.py"
    :return: a imported module from the aion core

    :since: 0.1.0
    """
    from . import is_aion

    if is_aion:
        from importlib import import_module
        from sys import path
        path.insert(0, aion_path + "/aion_core")
        return import_module(fname)
    else:
        no_aion()


def no_aion() -> None:
    """
    a function which get called from some 'aionlib' functions if aion is not installed but required

    :return: None

    :since: 0.1.0
    """
    pass


def start_check() -> None:
    """
    checks if system is linux and if aion is installed

    :return: None

    :since: 0.1.0
    """
    from colorama import Fore
    from os.path import isdir
    from platform import system

    if system().lower() != "linux":
        print(Fore.RED + "It seems like you not using Linux (Raspbian on Raspberry Pi recommended). To use the whole library run this library on Linux (recommended Raspbian on Raspberry Pi)" + Fore.RESET)
        start_check.is_linux = False
    else:
        start_check.is_linux = True

    if isdir(aion_path) is False:
        print(Fore.RED + "It seems like you haven't installed aion. To use the whole library install aion" + Fore.RESET)
        start_check.is_aion = False
    else:
        start_check.is_aion = True


class BaseXMLBuilder:
    """
    a class to simple build a '.xml' file

    :since: 0.1.0
    """

    def __init__(self, root_name: str = "root", **root_extra: str) -> None:
        """
        :param root_name: str, optional
            name of the root element of the xml file
            syntax: <root name>
            example: "root"
        :param root_extra: kwargs, optional
            attributes for the root element
            syntax: <key>=<value>
            example: author="blueShard"
        :return: None

        :since: 0.1.0
        """
        self.root_name = root_name

        self._element_list = [self.root_name]
        self._root = _ET.Element(root_name, **root_extra)

    def _prettify(self, string: str = None) -> str:
        """
        prettifies the given string

        :param string: str
            string to prettify
            syntax: <string>
            example: "<root><test_element></test_element></root>"
        :return: str
            returns the_prettified string
            syntax: <string>
            example: "<root>
                        <test_element>
                        </test_element>
                      </root>"

        :since: 0.1.0
        """
        if string is None:
            reparsed = _minidom.parseString(_ET.tostring(self._root, "utf-8"))
        else:
            reparsed = _minidom.parseString(bytes(string, "utf-8", errors="ignore"))
        pre_output = reparsed.toprettyxml(indent="  ")
        return "\n".join(pre_output.split("\n")[1:])

    def create_root_element(self, name: str, text: str = None, attrib: dict = {}, **extra: str) -> None:
        """
        creates a new entry as a sub element of the root element

        :param name: str
            name of the new element
            syntax: <name>
            example: "root_child"
        :param text: str, optional
            text of the new element
            syntax: <text>
            example: "This is a root element"
        :param attrib: dict, optional
            attributes for the new element
            syntax: {<key>, <value>}
            example: {"author": "blueShard"}
        :param extra: kwargs, optional
            attributes for the new element
            syntax: <key>=<value>
            example: author="blueShard"
        :return: None

        :since: 0.1.0
        """
        if text:
            element = _ET.Element(name, attrib, **extra).text = text
        else:
            element = _ET.Element(name, attrib, **extra)

        self._root.append(element)
        self._element_list.append(name)

    def create_sub_element(self, parent_name: str, name: str, text: str = None, attrib: dict = {}, parent_attrib: dict = None, **extra: str) -> None:
        """
        creates a sub element of an parent element

        :param parent_name: str
            name of the parent element to which the sub element should be added
            syntax: <parent name>
            example: "root_child"
        :param name: str
            name of the new sub element you want to add
            syntax: <name>
            example: "sub_child"
        :param text: str, optional
            text of the new sub element
            syntax: <text>
            example: "This is a sub element"
        :param attrib: dict, optional
            attributes for the new element
            syntax: {<key>, <value>}
            example: {"author": "blueShard"}
        :param parent_attrib: dict, optional
            attributes of the new sub element
            syntax: {<key>: <value>}
            example: {"language": "en_US"}
        :param extra: kwargs, optional
            attributes of the new sub element
            syntax: <key>=<value>
            example: language="en_US"
        :return: None

        :since: 0.1.0
        """

        if parent_name in self._element_list:
            for parent in self._root.iter(parent_name):
                if parent_attrib:
                    if parent.attrib == parent_attrib:
                        if text:
                            _ET.SubElement(parent, name, attrib, **extra).text = text
                        else:
                            _ET.SubElement(parent, name, attrib, **extra)
                        self._element_list.append(name)
                else:
                    if text:
                        _ET.SubElement(parent, name, attrib, **extra).text = text
                    else:
                        _ET.SubElement(parent, name, attrib, **extra)
                    self._element_list.append(name)
        else:
            raise IndexError("Couldn't find parent '" + parent_name + "'. The available parents are in this list: " + str(self._element_list))

    def get_string(self, pretty_print: bool = True) -> str:
        """
        get sting of the xml tree

        :param pretty_print: bool, optional
            sets True or False if the xml tree string should be pretty printed
            syntax: <boolean>
            example: True
        :return: str
            returns the string of the builded xml tree
            syntax: <xml tree>
            example: "<root>
                        <root_child author="blueShard">
                          <sub_child>This is a sub element</sub_child>
                        </root_child>
                      </root>"

        :since: 0.1.0
        """
        if pretty_print is True:
            return self._prettify()
        else:
            return _ET.tostring(self._root, "utf-8").decode("ascii")

    def write(self, fname: str, mode: str = "w", pretty_print: bool = True) -> None:
        """
        writes the xml tree to a file

        :param fname: str
            filename of file you want to write
            syntax: <filename>
            example: "/home/pi/text.xml"
        :param mode: str, optional
            mode to write on file
            syntax: <mode>
            example: "w"
        :param pretty_print: bool, optional
            sets True or False if the xml tree string should be pretty printed
            syntax: <boolean>
            example: True
        :return: None

        :since: 0.1.0
        """
        with open(fname, mode=mode) as file:
            file.write(self.get_string(pretty_print))
            file.close()


class BaseXMLReader:

    """
    a class to simple reead '.xml' file

    :since: 0.1.0
    """

    def __init__(self, fname: str) -> None:
        """
        makes the fname and auto_write available for all class methods and set all variables

        :param fname: str
            filename of the file you want to read
            syntax: <filename>
            example: "/home/pi/test.xml"
        :return: None

        :since: 0.1.0
        """
        self.fname = fname

        self._tree = _ET.parse(self.fname)
        self._root = self._tree.getroot()

        self.get_infos._root = self._root

    def _prettify(self, string: str = None) -> str:
        """
        prettifies the given string

        :param string: str
            string to prettify
            syntax: <string>
            example: "<root><test_element></test_element></root>"
        :return: str
            returns the_prettified string
            syntax: <string>
            example: "<root>
                        <test_element>
                        </test_element>
                      </root>"

        :since: 0.1.0
        """
        if string is None:
            reparsed = _minidom.parseString(_ET.tostring(self._root, "utf-8"))
        else:
            reparsed = _minidom.parseString(bytes(string, "utf-8", errors="ignore"))
        pre_output = reparsed.toprettyxml(indent="  ")
        return "\n".join(pre_output.split("\n")[1:])

    class get_infos(dict):
        """
        a modified dict class with indexing items

        :since: 0.1.0
        """

        def __init__(self, elem_tags: (str, list) = []) -> dict:
            """
            get infos about an element in the file

            :param elem_tags: list
                name of elements you want to get infos about
                syntax: [<element tags>]
                example: ["sub_child"]
            :return: dict
                returns a dict of names from the given elements with a list of dictionaries of found elements (complex description xD)
                syntax: {<element>: [{"parent": {"tag": <parent tag>, "text": <text of the parent element>, "attrib": {<attributes of the parent element>}}, "childs": [<childs of the element>], "tag": <tag of the element>, "text": <text of the element>, "attrib": {<attributes of the element>}}]}
                example: {"sub_child": [{"parent": {"tag": "root_child", "text": "", "attrib": {"author": "blueShard"}}, "childs": ["sub_child"], "tag": "sub_child", "text": "This is a sub element", "attrib": {}}]}

            :since: 0.1.0
            """
            if isinstance(elem_tags, str):
                elem_tags = [elem_tags]

            child_list = []
            return_dict = {}
            for elem in elem_tags:
                if elem == "<all>":
                    continue
                elif elem == "<root>":
                    return_dict[self._root.tag] = []
                else:
                    return_dict[elem] = []

            all_child_list = []

            if "<all>" in elem_tags:
                if self._root.tag in return_dict:
                    pass
                else:
                    return_dict[self._root.tag] = []
                return_dict[self._root.tag].append(
                    {"parent": {"tag": "", "text": "", "attrib": {}}, "childs": [child.tag for child in self._root], "tag": self._root.tag, "text": "", "attrib": self._root.attrib})
                for root_child in self._root:
                    if root_child.tag in return_dict:
                        pass
                    else:
                        return_dict[root_child.tag] = []
                    return_dict[root_child.tag].append(
                        {"parent": {"tag": self._root.tag, "text": self._root.text, "attrib": self._root.attrib}, "childs": [sub_root_child.tag for sub_root_child in root_child],
                         "tag": root_child.tag, "text": root_child.text, "attrib": root_child.attrib})
                    all_child_list.append(root_child)
                for parent in list(all_child_list):
                    for child in parent:
                        if child.tag in return_dict:
                            pass
                        else:
                            return_dict[child.tag] = []
                        return_dict[child.tag].append(
                            {"parent": {"tag": parent.tag, "text": parent.text, "attrib": parent.attrib}, "childs": [sub_child.tag for sub_child in child], "tag": child.tag, "text": child.text,
                             "attrib": child.attrib})
                        all_child_list.append(child)
                        if child in all_child_list:
                            all_child_list.remove(child)
            else:
                if self._root.tag in return_dict:
                    return_dict[self._root.tag].append({"parent": {}, "childs": [child.tag for child in self._root], "tag": self._root.tag, "text": "", "attrib": self._root.attrib})
                for root_child in self._root:
                    if root_child.tag in return_dict:
                        return_dict[root_child.tag].append(
                            {"parent": {"tag": self._root.tag, "text": self._root.text, "attrib": self._root.attrib}, "childs": [sub_root_child.tag for sub_root_child in root_child],
                             "tag": root_child.tag, "text": root_child.text, "attrib": root_child.attrib})
                    else:
                        child_list.append(root_child)
                for parent in list(child_list):
                    for child in parent:
                        if child.tag in return_dict:
                            return_dict[child.tag].append(
                                {"parent": {"tag": parent.tag, "text": parent.text, "attrib": parent.attrib}, "childs": [sub_child.tag for sub_child in child], "tag": child.tag, "text": child.text,
                                 "attrib": child.attrib})
                        else:
                            child_list.append(child)
                        if child in child_list:
                            child_list.remove(child)

            self._return_dict = return_dict

            self.items._return_dict_keys = return_dict.keys()
            self.items._return_dict_values = return_dict.values()
            self.keys._return_dict_keys = return_dict.keys()
            self.values._return_dict_values = return_dict.values()

            super().__init__(self._return_dict)

        def __iter__(self):
            return iter(self._return_dict)

        def __next__(self):
            return self._return_dict

        def __repr__(self):
            return self._return_dict

        def __str__(self):
            return str(self._return_dict)

        def index(self, index: int) -> dict:
            """
            index a key-value pair in a dict

            :param index: int
                index of the key-value pair you want to get
                syntax: <index>
                example: 5
            :return: dict
                returns the key-value pair of the given index
                syntax: {<key>: <value>}
                example: {"test_key": "test_value"}

            :since: 0.1.0
            """
            i = 0
            for key, value in self._return_dict.items():
                if i == index:
                    return {key: value}
                else:
                    i += 1
            raise IndexError("dict index out of range")

        class items:
            """
            a modified items() function from dict with indexing items

            :since: 0.1.0
            """

            def __init__(self):
                pass

            def __getitem__(self, item):
                return tuple(self._return_dict_items)[item]

            def __iter__(self):
                return iter(self._return_dict_items)

            def __len__(self):
                return len(self._return_dict_items)

            def __next__(self):
                return self._return_dict_items

            def __repr__(self):
                return self._return_dict_items

            def __str__(self):
                return str(self._return_dict_items)

            def index(self, index: int):
                """
                index a key-value pair in a dict

                :param index: int
                    index of the key-value pair you want to get
                    syntax: <index>
                    example: 5
                :return: the given index in the values

                :since: 0.1.0
                """
                return {list(self._return_dict_keys)[index]: list(self._return_dict_values)[index]}

        class keys:
            """
            a modified keys() function from dict with indexing items

            :since: 0.1.0
            """

            def __init__(self):
                pass

            def __iter__(self):
                return iter(self._return_dict_keys)

            def __len__(self):
                return len(list(self._return_dict_keys))

            def __next__(self):
                return self._return_dict_keys

            def __repr__(self):
                return self._return_dict_keys

            def __str__(self):
                return str(self._return_dict_keys)

            def index(self, index: int):
                """
                index a key in a dict

                :param index: int
                    index of the key you want to get
                    syntax: <index>
                    example: 5
                :return: the given index in the keys

                :since: 0.1.0
                """
                return list(self._return_dict_keys)[index]

        class values:
            """
            a modified values() function from dict with indexing items

            :since: 0.1.0
            """

            def __init__(self):
                pass

            def __iter__(self):
                return iter(self._return_dict_values)

            def __len__(self):
                return len(list(self._return_dict_values))

            def __next__(self):
                return self._return_dict_values

            def __repr__(self):
                return self._return_dict_values

            def __str__(self):
                return str(self._return_dict_values)

            def index(self, index: int):
                """
                index a value in a dict

                :param index: int
                    index of the value you want to get
                    syntax: <index>
                    example: 5
                :return: the given index in the values

                :since: 0.1.0
                """
                return list(self._return_dict_values)[index]

    def get_string(self, pretty_print: bool = True) -> str:
        """
        gets the string of the xml tree in the file

        :param pretty_print: bool, optional
            sets True or False if the xml tree string should be pretty printed
            syntax: <boolean>
            example: True
        :return: str
            returns the string of the xml tree
            syntax: <xml tree>
            example: "<root>
                        <root_child author="blueShard">
                          <sub_child>This is a sub element</sub_child>
                        </root_child>
                      </root>"

        :since: 0.1.0
        """
        string = _ET.tostring(self._root, "utf-8").decode("ascii")
        if pretty_print is True:
            if "\n" in string:
                return string
            else:
                return self._prettify()
        else:
            if "\n" in string:
                return "".join([line.strip() for line in _ET.tostring(self._root, "utf-8").decode("ascii").split("\n")])
            else:
                return string


class BaseXMLWriter:
    """
    a class to simple change/write a '.xml' file

    :since: 0.1.0
    """

    def __init__(self, fname: str, auto_write: bool = False) -> None:
        """
        :param fname: str
            filename of the file you want to write to
            syntax: <filename>
            example: "/home/pi/test.xml"
        :param auto_write: bool, optional
            sets if after every change to the getted xml tree the changes should be write to the file
            syntax: <boolean>
            example: False
        :return: None

        :since: 0.1.0
        """
        self.auto_write = auto_write
        self.fname = fname

        self._root = _ET.fromstring("".join([item.replace("\n", "").strip() for item in [line for line in open(self.fname, "r")]]))

    def _prettify(self, string: str = None) -> str:
        """
        prettifies the given string

        :param string: str
            string to prettify
            syntax: <string>
            example: "<root><test_element></test_element></root>"

        :return: str
            returns the_prettified string
            syntax: <string>
            example: "<root>
                        <test_element>
                        </test_element>
                      </root>"

        :since: 0.1.0
        """
        if string is None:
            reparsed = _minidom.parseString(_ET.tostring(self._root, "utf-8"))
        else:
            reparsed = _minidom.parseString(string)
        pre_output = reparsed.toprettyxml(indent="  ")
        return "\n".join(pre_output.split("\n")[1:])

    def add(self, parent_tag: str, elem_tag: str, text: str = None, attrib: dict = {}, parent_attrib: dict = None, **extra: str) -> None:
        """
        adds an element to xml tree

        :param parent_tag : str
            name of the parent element
            syntax: <parent name>
            example: "root_child"
        :param elem_tag : str
            name of the element you want to add
            syntax: <element name>
            example: "second_sub_child"
        :param text : str, optional
            text of the element you want to add
            syntax: <text>
            example: "This is the second sub child"
        :param attrib : dict
            attributes for the new element
            syntax: {<key>, <value>}
            example: {"author": "blueShard"}
        :param parent_attrib : dict, optional
            attributes of the parent element
            syntax: {<key>: <value>}
            example: {"author": "blueShard"}
        :param extra : kwargs, optional
            attributes of the new element
            syntax: <key>=<value>
            example: language="de_DE"
        :return: None

        :since: 0.1.0
        """
        if parent_tag == "<root>":
            parent_tag = self._root.tag

        if parent_tag == self._root.tag:
            if parent_attrib:
                if parent_attrib == self._root.attrib:
                    if text:
                        root_text_element = _ET.Element(elem_tag, attrib, **extra)
                        root_text_element.text = text
                        self._root.append(root_text_element)
                    else:
                        self._root.append(_ET.Element(elem_tag, attrib, **extra))
            else:
                if text:
                    root_text_element = _ET.Element(elem_tag, attrib, **extra)
                    root_text_element.text = text
                    self._root.append(root_text_element)
                else:
                    self._root.append(_ET.Element(elem_tag, attrib, **extra))
        else:
            for parent in self._root.iter(parent_tag):
                if parent_attrib:
                    if parent.attrib == parent_attrib:
                        if text:
                            _ET.SubElement(parent, elem_tag).text = text
                        else:
                            _ET.SubElement(parent, elem_tag, attrib, **extra)
                else:
                    if text:
                        _ET.SubElement(parent, elem_tag).text = text
                    else:
                        _ET.SubElement(parent, elem_tag, attrib, **extra)

        if self.auto_write is True:
            self.write()

    def get_string(self, pretty_print: bool = False) -> str:
        """
        gets the string of the xml tree in the file

        :param pretty_print: bool, optional
            sets True or False if the xml tree string should be pretty printed
            syntax: <boolean>
            example: True
        :return: str
            returns the string of the xml tree
            syntax: <xml tree>
            example: "<root>
                        <root_child author="blueShard">
                          <sub_child>This is a sub element</sub_child>
                          <second_sub_child language="de_DE"/>
                        </root_child>
                      </root>"

        :since: 0.1.0
        """
        string = _ET.tostring(self._root, "utf-8").decode("ascii")
        if pretty_print is True:
            if "\n" in string:
                return string
            else:
                return self._prettify()
        else:
            if "\n" in string:
                return "".join([line.strip() for line in _ET.tostring(self._root, "utf-8").decode("ascii").split("\n")])
            else:
                return string

    def remove(self, parent_tag: str, elem_tag: str, parent_attrib: dict = None) -> None:
        """
        removes an element from the xml tree

        :param parent_tag : str
            name of the parent element
            syntax: <parent name>
            example: "root_child"
        :param elem_tag : str
            name of the element you want to remove
            syntax: <element name>
            example: "second_sub_child"
        :param parent_attrib : dict, optional
            attributes of the parent element
            syntax: {<key>: <value>}
            example: {"author": "blueShard"}
        :return: None

        :since: 0.1.0
        """
        if parent_tag == "<root>":
            parent_tag = self._root.tag

        if parent_tag == self._root.tag:
            for child in self._root:
                if child.tag == elem_tag:
                    if parent_attrib:
                        if self._root.attrib == parent_attrib:
                            self._root.remove(child)
                    else:
                        self._root.remove(child)

        for parent in self._root.iter(parent_tag):
            for child in parent:
                if child.tag == elem_tag:
                    if parent_attrib:
                        if parent.attrib == parent_attrib:
                            parent.remove(child)
                    else:
                        parent.remove(child)

        if self.auto_write is True:
            self.write()

    def update(self, parent_tag: str, elem_tag: str, text: str = None, attrib: dict = {}, parent_attrib: dict = None, **extra: str) -> None:
        """
        updates an element in the xml tree

        :param parent_tag : str
            name of the parent element
            syntax: <parent name>
            example: "root_child"
        :param elem_tag : str
            name of the element you want to update
            syntax: <element name>
            example: "second_sub_child"
        :param text : str, optional
            new text of the updated element
            syntax: <text>
            example: "New text of the second sub child"
        :param attrib : dict
            attributes for the new element
            syntax: {<key>, <value>}
            example: {"author": "blueShard"}
        :param parent_attrib : dict, optional
            attributes of the parent element
            syntax: {<key>: <value>}
            example: {"author": "blueShard"}
        :param extra : kwargs, optional
           new attributes of the updated element
            syntax: <key>=<value>
            example: language="de_DE"
        :return: None

        :since: 0.1.0
        """
        if parent_tag == "<root>":
            parent_tag = self._root.tag

        if parent_tag == self._root.tag:
            for child in self._root:
                if child.tag == elem_tag:
                    if parent_attrib:
                        if self._root.attrib == parent_attrib:
                            if text:
                                child.text = str(text)
                            for key, value in attrib.items():
                                child.set(str(key), str(value))
                            for key, value in extra.items():
                                child.set(key, str(value))
                    else:
                        if text:
                            child.text = str(text)
                        for key, value in attrib.items():
                            child.set(str(key), str(value))
                        for key, value in extra.items():
                            child.set(key, str(value))
        for parent in self._root.iter(parent_tag):
            for child in parent:
                if child.tag == elem_tag:
                    if parent_attrib:
                        if parent.attrib == parent_attrib:
                            if text:
                                child.text = str(text)
                            for key, value in attrib.items():
                                child.set(str(key), str(value))
                            for key, value in extra.items():
                                child.set(key, str(value))
                    else:
                        if text:
                            child.text = str(text)
                        for key, value in attrib.items():
                            child.set(str(key), str(value))
                        for key, value in extra.items():
                            child.set(key, str(value))

        if self.auto_write is True:
            self.write()

    def write(self, mode: str = "w", pretty_print: bool = True) -> None:
        """
        writes the xml tree to a file

        :param mode : str, optional
            mode to write on file
            syntax: <mode>
            example: "w"
        :param pretty_print : bool, optional
            sets True or False if the xml tree string should be pretty printed
            syntax: <boolean>
            example: True
        :return: None

        :since: 0.1.0
        """
        with open(self.fname, mode=mode) as file:
            if pretty_print is False:
                file.write(_ET.tostring(self._root, "utf-8").decode("ascii"))
            else:
                file.write(self._prettify())
            file.close()
