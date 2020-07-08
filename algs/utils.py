import os

from typing import Iterable, Union


def app_dir():
    return os.path.dirname(os.path.abspath(__file__))


def code_block(path_to_file, markdown_lang=''):
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
