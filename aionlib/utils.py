#!/usr/bin/python3


def download_youtube_audio(url: str, path: str, output_format: str = "mp3") -> None:
    """
    downloads youtube audio by url

    :param url: str
        the url from which the audio should be downloaded
        syntax: <url>
        example: "https://youtu.be/MAlSjtxy5ak"
    :param path: str
        the path where the downloaded audio should be saved
        syntax: <path>
        example: "/home/pi/{title}"
        NOTE: in your path you can use the following things:
                "author"    channel name of the creator
                "category"  category of the video
                "dislikes"  number of dislikes on the video
                "duration"  duration time of the video (HH:MM:SS)
                "likes"     number of likes on the video
                "title"     title of the video
                "views"     number of views on the video
    :param output_format: str, optional
        output format of the audio
        syntax: <output format>
        example: "mp3"
    :return: None

    :since: 0.1.0
    """
    from . import is_aion
    from ._utils import no_aion
    if is_aion:
        from os import system
        from os.path import isdir, isfile
        from pafy import new
        from urllib.request import urlopen

        source = new(url)

        source_url = source.getbestaudio().url
        source_extension = source.getbestaudio().extension

        if isfile(path + "." + source_extension):
            raise FileExistsError(path + " must be an non existing file")
        elif isdir(path):
            raise IsADirectoryError("path must be path to file, not path to directory")

        path = path.format({"author": source.author, "category": source.category, "dislikes": source.dislikes, "duration": source.duration, "likes": source.likes, "title": source.title, "views": source.viewcount})
        with open(path + "." + source_extension, "wb") as file:
            file.write(bytes(urlopen(source_url).read()))
            file.close()

        system("ffmpeg -i " + path + "." + source_extension + " " + path + "." + output_format)
    else:
        no_aion()


def download_youtube_video(url: str, path: str, output_format: str = "mp4") -> None:
    """
    downloads youtube video by url

    :param url: str
        the url from which the video should be downloaded
        syntax: <url>
        example: "https://youtu.be/MAlSjtxy5ak"
    :param path: str
        the path where the downloaded video should be saved
        syntax: <path>
        example: "/home/pi/{title}"
        NOTE: in your path you can use the following things:
                "author"    channel name of the creator
                "category"  category of the video
                "dislikes"  number of dislikes on the video
                "duration"  duration time of the video (HH:MM:SS)
                "likes"     number of likes on the video
                "title"     title of the video
                "views"     number of views on the video
    :param output_format: str, optional
        output format of the video
        syntax: <output format>
        example: "mp4"
    :return: None

    :since: 0.1.0
    """
    from . import is_aion
    from ._utils import no_aion
    if is_aion:
        from os import system
        from os.path import isdir, isfile
        from pafy import new
        from urllib.request import urlopen

        source = new(url)

        source_url = source.getbestvideo().url
        source_extension = source.getbestvideo().extension

        if isfile(path + "." + source_extension):
            raise FileExistsError(path + " must be an not existing file")
        elif isdir(path):
            raise IsADirectoryError("path must be path to file, not path to directory")

        path = path.format({"author": source.author, "category": source.category, "dislikes": source.dislikes, "duration": source.duration, "likes": source.likes, "title": source.title, "views": source.viewcount})
        with open(path + "." + source_extension, "wb") as file:
            file.write(bytes(urlopen(source_url).read()))
            file.close()

        system("ffmpeg -i " + path + "." + source_extension + " " + path + "." + output_format)
    else:
        no_aion()


def get_full_directory_data(directory: str) -> list:
    """
    returns list of all files and directories of given directory back (subdirectories with subfiles, subsubdirectories with subsubfiles, ... included)

    :param directory: str
        path of directory from which you want to get the data
        syntax: <directory path>
        example: "/home/pi"

    :return: list
        list of all files and directories (subdirectories with subfiles, subsubdirectories with subsubfiles, ... included)
        syntax: [<path>]
        example: ["/home/pi/test", "/home/pi/test/test.py"]
    :return: None

    :since: 0.1.0
    """
    from os import walk
    from os.path import join

    data = []
    for path, subdirs, files in walk(directory):
        for name in files:
            data.append(join(path, name))
    return data


def get_full_youtube_audio_url(search_element: str) -> str:
    """
    search youtube for the search element and gives the first youtube url back

    :param search_element: str
        the element you want to search
        syntax: <search element>
        example: "Every programming tutorial"
    :return: str
        the youtube url from the search element
        syntax: <url>
        example: "https://youtu.be/MAlSjtxy5ak"

    :since: 0.1.0
    """
    import urllib.parse, urllib.request
    from pafy import new
    from re import findall
    search_query = urllib.parse.urlencode({"search_query": search_element})
    for i in range(10):  # sometimes the video url's cannot be found
        try:
            html_content = urllib.request.urlopen("https://www.youtube.com/results?" + search_query)
            search_results = findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            return new(str("https://www.youtube.com/watch?v=" + search_results[0])).getbestaudio().url
        except IndexError:
            pass


def get_full_youtube_video_url(search_element: str) -> str:
    """
    search youtube for the search element and gives the first youtube url back

    :param search_element: str
        the element you want to search
        syntax: <search element>
        example: "Every programming tutorial"
    :return: str
        the youtube url from the search element
        syntax: <url>
        example: "https://youtu.be/MAlSjtxy5ak"

    :since: 0.1.0
    """
    import urllib.parse, urllib.request
    from pafy import new
    from re import findall
    search_query = urllib.parse.urlencode({"search_query": search_element})
    for i in range(10):  # sometimes the video url's cannot be found
        try:
            html_content = urllib.request.urlopen("https://www.youtube.com/results?" + search_query)
            search_results = findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
            return new(str("https://www.youtube.com/watch?v=" + search_results[0])).getbestvideo().url
        except IndexError:
            pass


def get_line_number(fname: str, search_element: str, full_line: bool = True, strip: bool = True) -> int:
    """
    returns the line number of an element in a file

    :param fname: str
        name of the file you want to search for the element
        syntax: <file name>
        example: "test_file"
    :param search_element: str
        element you want to get the line number of
        syntax: <search element>
        example: "test_search_element"
    :param full_line: bool
        sets if the 'search_element' should be the FULL line (True) or if the 'search_element' should be IN the line (False)
        syntax: <boolean>
        example: False
    :param strip: bool
        sets if the line of the should be striped before search the 'search_element' in it
        syntax: <boolean>
        example: False
    :return: int
        returns the line number of the 'search_element'
        syntax: <line number>
        example: 69

    :since: 0.1.0
    """
    from os.path import isfile
    if isfile(fname) is False:
        raise FileNotFoundError(fname + " don't exist")
    line_number = -1
    if full_line and strip:
        for line in open(fname):
            line_number = line_number + 1
            if line.strip() == search_element:
                return line_number
    elif full_line and strip is False:
        for line in open(fname):
            line_number = line_number + 1
            if line == search_element:
                return line_number
    elif full_line is False and strip:
        for line in open(fname):
            line_number = line_number + 1
            if search_element in line.strip():
                return line_number
    else:
        for line in open(fname):
            line_number = line_number + 1
            if search_element in line:
                return line_number

    raise EOFError("couldn't get line number of " + search_element)


def get_youtube_url(search_element: str) -> str:
    """
    search youtube for the search element and gives the first youtube url back

    :param search_element: str
        the element you want to search
        syntax: <search element>
        example: "Every programming tutorial"
    :return: str
        the youtube url from the search element
        syntax: <url>
        example: "https://youtu.be/MAlSjtxy5ak"

    :since: 0.1.0
    """
    import re, urllib.parse, urllib.request
    search_query = urllib.parse.urlencode({"search_query": search_element})
    html_content = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_query)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
    return str("https://www.youtube.com/watch?v=" + search_results[0])


def is_dict_in_dict(dict1: dict, dict2: dict) -> bool:
    """
    checks if dict key-value pairs exist in another dict

    :param dict1: dict
        dictionary you want to check if it is included in another dictionary
        syntax: {"key": "value"}
        example: {"a": "b"}
    :param dict2: dict
        dictionary you want to see if there is another dictionary in it
        syntax: {"key": "value"}
        example: {"a": "b", "c": "d"}
    :return: boolean
        returns if 'dict1' is in 'dict2'
        syntax: <boolean>
        example: True

    :since: 0.1.0
    """
    for key, value in dict1.items():
        if key in dict2:
            if dict2[key] == value:
                pass
            else:
                return False
        else:
            return False

    return True


def is_element_in_file(fname: str, element: str) -> bool:
    """
    checks if an element is in a file

    :param fname: str
        file name of file
        syntax: <file name>
        example: "/home/pi/test.py"
    :param element: str
        element you want to check if in file
        syntax: <element>
        example: "test"
    :return: bool
        returns True or False is element is in file
        syntax: <boolean>
        example: True

    :since: 0.1.0
    """
    is_in_file = False
    for line in open(fname, "r"):
        if element in line:
            is_in_file = True
            break
    return is_in_file


def is_internet_connected() -> bool:
    """
    checks if the internet is connected

    :return: bool
        returns True or False if internet is connected
        syntax: <boolean>
        example: True

    :since: 0.1.0
    """
    import socket
    try:
        socket.gethostbyname("google.com")
        internet = True
    except OSError:
        internet = False
    except:
        internet = False
        print("An unexpected error appeard")
    return internet


def is_root() -> bool:
    """
    checks if the function from which this function is called run as root

    :return: bool
        returns True or False if the function from which this function is called run as root
        syntax: <boolean>
        example: True

    :since: 0.1.0
    """
    from os import geteuid
    if geteuid() == 0:
        return True
    elif geteuid() == 1000:
        return False


def remove_brackets(string: str) -> str:
    """
    removes all brackets and the text which is between the brackets

    :param string: str
        string from which you want to remove the brackets
        syntax: <string>
        example: "Hello, this is(wedcwerfwe) an [sdvsfvv] random text{ervweg}"
    :return: str
        string without brackets and the text between them
        syntax: <string without brackets>
        example: "Hello, this is an random text"

    :since: 0.1.0
    """
    finished_string = ""
    square_brackets = 0
    parentheses = 0
    for brackets in string:
        if brackets == "[":
            square_brackets += 1
        elif brackets == "(":
            parentheses += 1
        elif brackets == "]" and square_brackets > 0:
            square_brackets -= 1
        elif brackets == ")" and parentheses > 0:
            parentheses -= 1
        elif square_brackets == 0 and parentheses == 0:
            finished_string += brackets
    return finished_string


def remove_space(string: str, space: str = "  ") -> str:
    """
    removes all the space from string which is equal or higher than from argument 'space' given space

    :param string: str
        string from which you want to remove space
        syntax: <string>
        example: "This string has     to   much space"
    :param space: str, optional
        space size from which you want to start to remove
        syntax: <space>
        example: "  "
        NOTE: '"  "' will be replaced with '" "'
    :return: str
        returns the string without the given space and higher
        syntax: <string>
        example: "This string has to much space"

    :since: 0.1.0
    """
    while True:
        if space in string:
            string = string.replace(space, "")
        space = space + " "
        if len(space) >= len(string):
            break

    string = string.strip()
    return string


def remove_string_characters(string: str, characters_to_remove: (list, tuple)) -> str:
    """
    removes in argument 'characters_to_remove' given characters from given string

    :param string: str
        string from which you want to remove the characters
        syntax: <string>
        example: "This string hello has its to much word me"
    :param characters_to_remove: list
        list of characters you want to remove from string
        syntax: [<character>]
        example: ["hello", "its", "me"]
    :return: str
        returns string without in given characters to remove
        syntax: <string>
        example: "This string has to much word"

    :since: 0.1.0
    """
    for char in characters_to_remove:
        if char in string:
            string = string.replace(char, "")
    return string


def remove_string_sequence(string: str, start: str, end: str, include: bool = False) -> str:
    """
    removes all characters from a string between the given 'start' and 'end' element

    :param string: str
        the string from which the sequence should be removed from
        syntax: "<string>"
        example: "Test lol random words string"
    :param start: str
        start character
        syntax: "<start character>"
        example: "lol"
    :param end: str
        end character
        syntax: "<end character>"
        example: "words"
    :param include: bool
        'True' if the given start and end character should be included in the return string, False if not
        syntax: <boolean>
        example: False
    :return: str
        string without the sequence between 'start' and 'end'
        syntax: "<string>"
        example: "Test  string"

    :since: 0.1.0
    """
    if include:
        return string.replace(string[string.find(start) - len(start):string.find(end)], "")
    return string.replace(string[string.find(start):string.find(end) + len(end)], "")


def replace_line(fname: str, line_number: int, new_line: str) -> None:
    """
    replaces a line in a file

    :param fname: str
        filename from which you want to replace the line
        syntax: <filename>
        example: "/home/pi/test.txt"
    :param line_number: int
        line number of line you want to replace
        syntax: <line number>
        example: 5
    :param new_line: str
        line content with which the line should be replaced
        syntax: <new line>
        example: "This is the new line"
    :return: None

    :since: 0.1.0
    """
    from os.path import isfile

    line_number = int(line_number)
    if isfile(fname) is False:
        raise FileNotFoundError(fname + " don't exist")
    lines = open(fname).readlines()
    lines[line_number] = new_line + "\n"
    with open(fname, "w") as file:
        file.writelines(lines)
        file.close()


def vlc(url_or_file_path: str, video: bool = False) -> None:
    """
    plays audio from url or file path

    :param url_or_file_path: str
        the url or the path of the file you want to play
        syntax: <url or path>
        example: "https://youtu.be/MAlSjtxy5ak"
    :param video: bool, optional
        sets True or False if video should be played (if the file had one)
        syntax: <boolean>
        example: False
    :return: None

    :since: 0.1.0
    """
    from os import system

    if isinstance(video, bool) is False:
        raise TypeError("expected " + str(bool.__name__) + " for video, got " + str(type(video).__name__))
    if video is True:
        system("cvlc --play-and-exit " + url_or_file_path)
    else:
        system("cvlc --play-and-exit --no-video " + url_or_file_path)
