#!/usr/bin/python3

from . import aion_data_path, is_aion
from ._utils import no_aion
from time import time as _time


class LogAion:
    """
    class for adding own logs to the aion logger

    :since: 0.1.0
    """

    def __init__(self) -> None:
        """
        set all class variables

        :return: None

        :since: 0.1.0
        """
        if is_aion:
            from ._utils import import_aion_internal_file as _import_aion_internal_file
            self._aion_logger = _import_aion_internal_file("logging").LogAll(aion_data_path + "/logs/aion.log",
                                                                             critical_fname=aion_data_path + "/logs/critical.log",
                                                                             debug_fname=aion_data_path + "/logs/debug.log",
                                                                             error_fname=aion_data_path + "/logs/error.log",
                                                                             info_fname=aion_data_path + "/logs/info.log",
                                                                             warning_fname=aion_data_path + "/logs/warning.log")

    def critical(self, msg: str, lineno: int = None) -> None:
        """
        prints and write given format with 'critical' levelname and in 'msg' given message

        :param msg: str
            message you want to print and write
            syntax: <message>
            example: "critical message"
        :param lineno: int, optional
            custom 'lineno' (line number) entry
            syntax: <lineno>
            example: 5
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_logger.critical(msg=msg, lineno=lineno)
        else:
            no_aion()

    def debug(self, msg: str, lineno: int = None) -> None:
        """
        prints and write given format with 'debug' levelname and in 'msg' given message

        :param msg: str
            message you want to print and write
            syntax: <message>
            example: "debug message"
        :param lineno: int, optional
            custom 'lineno' (line number) entry
            syntax: <lineno>
            example: 5
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_logger.debug(msg=msg, lineno=lineno)
        else:
            no_aion()

    def error(self, msg: str, lineno: int = None) -> None:
        """
        prints and write given format with 'error' levelname and in 'msg' given message

        :param msg: str
            message you want to print and write
            syntax: <message>
            example: "error message"
        :param lineno: int, optional
            custom 'lineno' (line number) entry
            syntax: <lineno>
            example: 5
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_logger.error(msg=msg, lineno=lineno)
        else:
            no_aion()

    def info(self, msg: str, lineno: int = None) -> None:
        """
        prints and write given format with 'info' levelname and in 'msg' given message

        :param msg: str
            message you want to print and write
            syntax: <message>
            example: "info message"
        :param lineno: int, optional
            custom 'lineno' (line number) entry
            syntax: <lineno>
            example: 5
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_logger.info(msg=msg, lineno=lineno)
        else:
            no_aion()

    def warning(self, msg: str, lineno: int = None) -> None:
        """
        prints and write given format with 'warning' levelname and in 'msg' given message

        :param msg: str
            message you want to print and write
            syntax: <message>
            example: "warning message"
        :param lineno: int, optional
            custom 'lineno' (line number) entry
            syntax: <lineno>
            example: 5
        :return: None

        :since: 0.1.0
        """
        if is_aion:
            self._aion_logger.warning(msg=msg, lineno=lineno)
        else:
            no_aion()


class LogConsole:
    """
    a simple logger for consoles

    :since: 0.1.0
    """

    def __init__(self, format: str = "[{runtime}] - {filename}(line: {lineno}) - {levelname}: {message}") -> None:
        """
        :param format : str, optional
            format of the console output
            syntax: <format>
            example: [{runtime}] - {filename}(line: {lineno}) - {levelname}: {message}
            NOTE: in 'format' you can use the following curly bracktes:
                year            gives the year back
                month           gives the month back
                day             gives the day back
                hour            gives the hour back
                minute          gives the minute back
                second          gives the second back
                microsecond     gives the microsecond back
                runtime         gives the back since the logger has started
                levelname       gives the levelname back
                filename        gives the name of the file from which the logger is called back
                lineno          gives the line number back from which the levelname function was called
                function        gives the function back from which the levelname function was called
                message         gives the in levelname function given message back
        :return: None

        :since: 0.1.0
        """
        from datetime import datetime
        from inspect import getframeinfo, stack

        self.format = format

        self._caller_infos = getframeinfo(stack()[1][0])
        self._date = datetime.now()
        self._start_time = _time()

    def _format(self, levelname: str, message: str) -> dict:
        """
        returns a dict with custom entries

        :param levelname: str
            name of the level
            syntax: <levelname>
            example: "INFO"
        :param message: str
            message in the dict
            syntax: <message>
            example: "Test message"

        :return: dict
            syntax: {"year": <year>,
                     "month": <month>,
                     "day": <day>,
                     "hour": <hour>,
                     "minute": <minute>,
                     "second": <second>,
                     "microsecond": <microsecond>,
                     "runtime": <runtime>,
                     "levelname": <level name>,
                     "filename": <filename>,
                     "lineno": <line number>,
                     "function": <function>,
                     "message": <message>}
            example: {"year": 2000,
                      "month": 1,
                      "day": 1,
                      "hour": 00,
                      "minute": 00,
                      "second": 00,
                      "microsecond": 00000,
                      "runtime": "01:23:45",
                      "levelname": "INFO",
                      "filename": "abc.py",
                      "lineno": 123,
                      "function": "test_function",
                      "message": "This is a test message"}

        :since: 0.1.0
        """
        return {"year": self._date.year, "month": self._date.month, "day": self._date.day, "hour": self._date.hour, "minute": self._date.minute, "second": self._date.second, "microsecond": self._date.microsecond,
                "runtime": self._runtime(), "levelname": levelname, "filename": self._caller_infos.filename, "lineno": self._caller_infos.lineno, "function": self._caller_infos.function, "message": message}

    def _runtime(self) -> str:
        """
        returns the runtime

        :return: str
            returns the runtime
            syntax: <hour>:<minute>:<day>
            example: "01:23:45"

        :since: 0.1.0
        """
        second = int(_time() - self._start_time)
        minute = 0
        hour = 0
        while (second / 60) >= 1:
            minute += 1
            second -= 60

        while (minute / 60) >= 1:
            hour += 1
            minute -= 60

        if len(str(second)) == 1:
            second = "0" + str(second)

        if len(str(minute)) == 1:
            minute = "0" + str(minute)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)

        return str(str(hour) + ":" + str(minute) + ":" + str(second))

    def critical(self, msg: str, _format_values: dict = None) -> None:
        """
        prints given format with 'critical' levelname and in 'msg' given message

        :param msg: str
            message you want to print out
            syntax: <message>
            example: "critical message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            print(self.format.format(**self._format(levelname="CRITICAL", message=msg)))
        else:
            print(self.format.format(**_format_values))

    def debug(self, msg: str, _format_values: dict = None) -> None:
        """
        prints given format with 'debug' levelname and in 'msg' given message

        :param msg: str
            message you want to print out
            syntax: <message>
            example: "debug message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            print(self.format.format(**self._format(levelname="DEBUG", message=msg)))
        else:
            print(self.format.format(**_format_values))

    def error(self, msg: str, _format_values: dict = None) -> None:
        """
        prints given format with 'error' levelname and in 'msg' given message

        :param msg: str
            message you want to print out
            syntax: <message>
            example: "error message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            print(self.format.format(**self._format(levelname="ERROR", message=msg)))
        else:
            print(self.format.format(**_format_values))

    def info(self, msg: str, _format_values: dict = None) -> None:
        """
        prints given format with 'info' levelname and in 'msg' given message

        :param msg: str
            message you want to print out
            syntax: <message>
            example: "info message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            print(self.format.format(**self._format(levelname="INFO", message=msg)))
        else:
            print(self.format.format(**_format_values))

    def warning(self, msg: str, _format_values: dict = None) -> None:
        """
        prints given format with 'warning' levelname and in 'msg' given message

        :param msg: str
            message you want to print out
            syntax: <message>
            example: "warning message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """

        if _format_values is None:
            print(self.format.format(**self._format(levelname="WARNING", message=msg)))
        else:
            print(self.format.format(**_format_values))


class LogFile:
    """
    a simple logger for files

    :since: 0.1.0
    """

    def __init__(self, log_fname: str, mode: str = "a", format: str = "[{year}-{month}-{day} {hour}:{minute}:{second}] - {filename}(line: {lineno}) - {levelname}: {message}") -> None:
        """
        :param log_fname: str
            filename of the file to which the logging messages should be saved
            syntax: <fname>
            example: "/home/pi/test.log"
        :param mode: str, optional
            mode to write on file
            syntax: <mode>
            example: "a"
        :param format: str, optional
            format of the output that should be write to file
            syntax: <format>
            example: [{runtime}] - {filename}(line: {lineno}) - {levelname}: {message}
            NOTE: in 'format' you can use the following curly bracktes:
                year            gives the year back
                month           gives the month back
                day             gives the day back
                hour            gives the hour back
                minute          gives the minute back
                second          gives the second back
                microsecond     gives the microsecond back
                runtime         gives the back since the logger has started
                levelname       gives the levelname back
                filename        gives the name of the file from which the logger is called back
                lineno          gives the line number back from which the levelname function was called
                function        gives the function back from which the levelname function was called
                message         gives the in levelname function given message back
        :return: None

        :since: 0.1.0
        """
        from datetime import datetime
        from inspect import getframeinfo, stack

        self.format = format
        self.log_fname = log_fname
        self.mode = mode

        self._caller_infos = getframeinfo(stack()[1][0])
        self._date = datetime.now()
        self._start_time = _time()

    def _format(self, levelname: str, message: str) -> dict:
        """
        returns a dict with custom entries

        :param levelname: str
            name of the level
            syntax: <levelname>
            example: "INFO"
        :param message: str
            message in the dict
            syntax: <message>
            example: "Test message"
        :return: dict
            syntax: {"year": <year>,
                     "month": <month>,
                     "day": <day>,
                     "hour": <hour>,
                     "minute": <minute>,
                     "second": <second>,
                     "microsecond": <microsecond>,
                     "runtime": <runtime>,
                     "levelname": <level name>,
                     "filename": <filename>,
                     "lineno": <line number>,
                     "function": <function>,
                     "message": <message>}
            example: {"year": 2000,
                      "month": 1,
                      "day": 1,
                      "hour": 00,
                      "minute": 00,
                      "second": 00,
                      "microsecond": 00000,
                      "runtime": "01:23:45",
                      "levelname": "INFO",
                      "filename": "abc.py",
                      "lineno": 123,
                      "function": "test_function",
                      "message": "This is a test message"}

        :since: 0.1.0
        """
        return {"year": self._date.year, "month": self._date.month, "day": self._date.day, "hour": self._date.hour, "minute": self._date.minute, "second": self._date.second, "microsecond": self._date.microsecond,
                "runtime": self._runtime(), "levelname": levelname, "filename": self._caller_infos.filename, "lineno": self._caller_infos.lineno, "function": self._caller_infos.function, "message": message}

    def _runtime(self) -> str:
        """
        returns the runtime

        :return: str
            returns the runtime
            syntax: <hour>:<minute>:<day>
            example: "01:23:45"

        :since: 0.1.0
        """
        second = int(_time() - self._start_time)
        minute = 0
        hour = 0
        while (second / 60) >= 1:
            minute += 1
            second -= 60

        while (minute / 60) >= 1:
            hour += 1
            minute -= 60

        if len(str(second)) == 1:
            second = "0" + str(second)

        if len(str(minute)) == 1:
            minute = "0" + str(minute)

        if len(str(hour)) == 1:
            hour = "0" + str(hour)

        return str(str(hour) + ":" + str(minute) + ":" + str(second))

    def _write(self, msg: str) -> None:
        """
        writes the given message to the log file

        :param msg: str
            message that should be write to the file
            syntax: <message>
            example: "Test message"
        :return: None

        :since: 0.1.0
        """
        with open(self.log_fname, self.mode) as file:
            file.write(msg + "\n")
            file.close()

    def critical(self, msg: str, _format_values: dict = None) -> None:
        """
        writes given format with 'critical' levelname and in 'msg' given message to file

        :param msg: str
            message you want to write to file
            syntax: <message>
            example: "critical message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            self._write(self.format.format(**self._format(levelname="CRITICAL", message=msg)))
        else:
            self._write(self.format.format(**_format_values))

    def debug(self, msg: str, _format_values: dict = None) -> None:
        """
        writes given format with 'debug' levelname and in 'msg' given message to file

        :param msg: str
            message you want to write to file
            syntax: <message>
            example: "debug message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            self._write(self.format.format(**self._format(levelname="DEBUG", message=msg)))
        else:
            self._write(self.format.format(**_format_values))

    def error(self, msg: str, _format_values: dict = None) -> None:
        """
        writes given format with 'debug' levelname and in 'msg' given message to file

        :param msg: str
            message you want to write to file
            syntax: <message>
            example: "debug message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            self._write(self.format.format(**self._format(levelname="ERROR", message=msg)))
        else:
            self._write(self.format.format(**_format_values))

    def info(self, msg: str, _format_values: dict = None) -> None:
        """
        writes given format with 'info' levelname and in 'msg' given message to file

        :param msg: str
            message you want to write to file
            syntax: <message>
            example: "info message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            self._write(self.format.format(**self._format(levelname="INFO", message=msg)))
        else:
            self._write(self.format.format(**_format_values))

    def warning(self, msg: str, _format_values: dict = None) -> None:
        """
        writes given format with 'warning' levelname and in 'msg' given message to file

        :param msg: str
            message you want to write to file
            syntax: <message>
            example: "warning message"
        :param _format_values: dict, optional
            dictionary with own format values
            syntax: {<key>: <value>}
            example: {"mytext": "This is my text"}
            NOTE: if you use '_format_values' the in function '_format' given format values won't used
        :return: None

        :since: 0.1.0
        """
        if _format_values is None:
            self._write(self.format.format(**self._format(levelname="WARNING", message=msg)))
        else:
            self._write(self.format.format(**_format_values))
