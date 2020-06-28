#!/usr/bin/python3

from . import is_linux


_aion_variable_file = "/tmp/aion39ewefv90erfte25"

_default_variables = {"IS_AION_RUNNING": False}

IS_AION_RUNNING = "IS_AION_RUNNING"


class Variable:
    """
    base class for aion variables

    :since: 0.1.0
    """

    def __init__(self) -> None:
        """
        set all class variables

        :return: None

        :since: 0.1.0
        """
        from . import is_linux
        from os.path import isfile as _isfile

        self._user_variables = {}

        if _isfile(_aion_variable_file) and is_linux is False:
            self._aion_open_variable_file = open(_aion_variable_file, "rw")
        else:
            self._aion_open_variable_file = None

    def add_variable(self, variable_name, value):
        """
        adds a variable

        :param variable_name: str
            name of the variable you want to add
            syntax: <variable name>
            example: "test_variable"
        :param value: str
            value of the variable
            syntax: <value>
            example: "test_value"
        :return: None

        :since: 0.1.0
        """
        if self._aion_open_variable_file is not None:
            file = open(_aion_variable_file, "a")
            file.write(variable_name + "=" + value)
            self._aion_open_variable_file = open(_aion_variable_file, "rw")
        self._user_variables[variable_name] = value

    def close(self):
        """
        remove the file with the saved variables

        :return: None

        :since: 0.1.0
        """
        from os import remove

        if self._aion_open_variable_file is not None:
            remove(_aion_variable_file)
            self._aion_open_variable_file = None

    def get_value(self, variable_name):
        """
        get the value of an variable

        :param variable_name: str
            name of the variable you want to get the value
            syntax: <variable name>
            example: "test_variable"
        :return: str
            return the value of the variable
            syntax: <value>
            example: <text_variable_value>

        :since: 0.1.0
        """
        if self._aion_open_variable_file is not None:
            for value in self._aion_open_variable_file:
                if value.strip().startswith("#"):
                    continue
                elif value.split("=")[0].strip() == variable_name:
                    return value.split("=")[1].strip()
            raise KeyError("the variable " + variable_name + " doesn't exists")
        else:
            try:
                return _default_variables[variable_name]
            except KeyError:
                if variable_name in self._user_variables:
                    return self._user_variables[variable_name]
                raise KeyError("the variable " + variable_name + " doesn't exists")

    def inititalize_variables(self, additional_variables={}):
        """
        creates a new file for the variables to store

        :param additional_variables: dict, optional
            variables that should be added ('add_variable' could be used instead)
            syntax: {"key": "value"}
            example: {"test": "True"}
        :return: None

        :since: 0.1.0
        """
        if is_linux:
            self._aion_open_variable_file = open(_aion_variable_file, "w+")
            write_list = [variable + "=" + str(value) for variable, value in _default_variables.items()]
            write_list = write_list + [str(additional_variable) + "=" + str(additional_value) for additional_variable, additional_value in additional_variables.items()]
            write_list = write_list + [str(user_variable) + "=" + str(user_value) for user_variable, user_value in self._user_variables]
            self._aion_open_variable_file.writelines(write_list)
            self._aion_open_variable_file = open(_aion_variable_file, "w+")

    def remove_variable(self, variable_name):
        """
        removes a variable

        :param variable_name: str
            name of the variable
            syntax: <variable name>
            example: "test_variable"
        :return: None

        :since: 0.1.0
        """
        try:
            from .utils import remove_space, replace_line
        except ImportError:
            from utils import remove_space, replace_line

        found = False

        if variable_name in self._user_variables:
            del self._user_variables[variable_name]
            found = True

        if self._aion_open_variable_file is not None:
            line_number = -1
            for line in self._aion_open_variable_file:
                line_number = line_number + 1
                if remove_space(line, "").split("=")[0] == variable_name:
                    replace_line(_aion_variable_file, line_number, "")
                    self._aion_open_variable_file = open(_aion_variable_file, "rw")
                    return

        if found is False:
            raise KeyError("the variable " + variable_name + " doesn't exists")

    def set_value(self, variable_name, value):
        """
        set a new value to a variable

        :param variable_name: str
            name of the variable you want to change the value
            syntax: <variable name>
            example: "test_variable"
        :param value: str
            new value
            syntax: <new value>
            example: "new_test_value"
        :return: None

        :since: 0.1.0
        """
        try:
            from .utils import remove_space, replace_line
        except ImportError:
            from utils import remove_space, replace_line

        found = False

        if variable_name in self._user_variables:
            self._user_variables[variable_name] = value
            found = True

        line_number = -1
        for line in self._aion_open_variable_file:
            line_number = line_number + 1
            if remove_space(line, "").split("=")[0] == variable_name:
                replace_line(_aion_variable_file, line_number, variable_name + "=" + value)
                self._aion_open_variable_file = open(_aion_variable_file, "rw")
                return

        if found is False:
            raise KeyError("the variable " + variable_name + " doesn't exists")
