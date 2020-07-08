import os

from typing import Iterable, Union


def app_dir():
    """
    :return: the absolute path of the directory containing the main streamlit app
    """
    return os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))


def code_block(path_to_file, markdown_lang=''):
    """
    Open a file and format the contents as a markdown code block of specified language. If the file
    cannot be opened, a message will be returned indicating that.

    :param path_to_file: path to the file containing code to be included
    :param markdown_lang: (optional) language of markdown code block
    :return: formatted markdown code block containing the contents of the file
    """
    if os.path.isfile(path_to_file):
        file_content = open(path_to_file, 'r').read().strip()
        return f"```{markdown_lang}\n{file_content}\n```"
    else:
        return f'Cannot find file {path_to_file}'


def format_from_lang(to_format: Union[Iterable[str], str]):
    if isinstance(to_format, str):
        if to_format == 'C++':
            return 'cpp'
        else:
            return to_format.lower()
    else:
        return [format_from_lang(x) for x in to_format]


def format_from_title(to_format: Union[Iterable[str], str]):
    if isinstance(to_format, str):
        return to_format.lower().replace(' ', '_')
    else:
        return [format_from_title(x) for x in to_format]


def format_to_lang(to_format: Union[Iterable[str], str]):
    if isinstance(to_format, str):
        if to_format == 'cpp':
            return 'C++'
        else:
            return to_format.title()
    else:
        return [format_to_lang(x) for x in to_format]


def format_to_title(to_format: Union[Iterable[str], str]):
    """
    Take a string or iterable of strings and convert to title case, replacing any underscores with
    spaces.

    :param to_format: the string or iterable of strings to format
    :return: formatted string or list of strings
    """
    if isinstance(to_format, str):
        return to_format.title().replace('_', ' ')
    else:
        return [format_to_title(x) for x in to_format]


def get_all_algorithms():
    alg_dirs = [x for x in os.listdir(os.path.join(app_dir(), 'algs')) if not x.startswith('_')]
    return sorted([alg for alg in alg_dirs if os.path.isdir(os.path.join(app_dir(), 'algs', alg))])


def get_all_languages():
    lang_dirs = os.listdir(os.path.join(app_dir(), 'code'))
    return sorted([lang for lang in lang_dirs if os.path.isdir(os.path.join(
        app_dir(), 'code', lang))])


def get_file_extension(language: str):
    extension_lookup = {
        'cpp': 'hpp',
        'julia': 'jl',
        'python': 'py',
        'rust': 'rs',
    }
    return extension_lookup[language]


def get_implemented_algorithms():
    algs = {}
    for alg in get_all_algorithms():
        algs[alg] = []
        for lang in get_all_languages():
            if os.path.isdir(os.path.join(app_dir(), 'code', lang, alg)):
                algs[alg].append(lang)
    return algs


def markdown_content(path_to_file):
    if os.path.isfile(path_to_file):
        return open(path_to_file, 'r').read().strip()
    else:
        return f'Cannot find file {path_to_file}'
