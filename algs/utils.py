import os
import yaml


def app_dir():
    """
    :return: the absolute path of the directory containing the main streamlit app
    """
    return os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir))


"""
Load the manifest files once only
"""
manifest_algs = yaml.safe_load(open(os.path.join(app_dir(), 'manifest_algs.yaml'), 'r').read())
manifest_code = yaml.safe_load(open(os.path.join(app_dir(), 'manifest_code.yaml'), 'r').read())


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


def format_alg_name(to_format: str):
    """
    Take a string representing the canonical name of an algorithm (e.g. forward_euler) and return
    its display name (e.g. Forward Euler).

    :param to_format: the canonical algorithm name
    :return: the algorithm's display name
    """
    return manifest_algs.get(to_format).get('display')


def format_lang_name(to_format: str):
    """
    Take a string representing the canonical name of a language (cpp, python, etc) and return its
    formatted name (C++, Python, etc).

    :param to_format: the canonical language name
    :return: the formatted language name
    """
    return manifest_code.get(to_format).get('display')


def get_all_algorithms():
    """
    :return: The list of all algorithms
    """
    return sorted(manifest_algs.keys())


def get_all_languages():
    """
    :return: The list of all languages that have implemented at least one algorithm
    """
    return sorted(manifest_code.keys())


def get_file_extension(language: str):
    """
    Get the file extension for a given language.

    :param language: the language
    :return: the corresponding file extension
    """
    return manifest_code.get(language).get('ext')


def implementations(algorithm: str):
    """
    Get all languages with an implementation for the given algorithm

    :param algorithm: the algorithm
    :return: list of languages with an implementation for the given algorithm
    """
    return manifest_algs.get(algorithm).get('impl')


def markdown_content(path_to_file):
    if os.path.isfile(path_to_file):
        return open(path_to_file, 'r').read().strip()
    else:
        return f'Cannot find file {path_to_file}'
