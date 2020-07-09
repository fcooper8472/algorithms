import importlib
import os
import sys
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


def display_alg_content(algorithm: str):
    """
    If the module algs.{algorithm} exists and contains a method {algorithm}_content, then call that
    function, else do nothing.
    :param algorithm:
    :return:
    """
    if not os.path.isfile(os.path.join(app_dir(), 'algs', algorithm, '__init__.py')):
        return
    importlib.import_module(f'algs.{algorithm}')
    alg_module = sys.modules.get(f'algs.{algorithm}')
    if alg_module:
        method_name = f'{algorithm}_content'
        if hasattr(alg_module, method_name):
            getattr(alg_module, method_name)()


def format_alg_name(to_format: str):
    """
    Take a string representing the canonical name of an algorithm (e.g. forward_euler) and return
    its display name (e.g. Forward Euler). Any other string is converted to title case.

    :param to_format: the canonical algorithm name
    :return: the algorithm's display name
    """
    alg_entry = manifest_algs.get(to_format)
    return alg_entry.get('display') if alg_entry else to_format.title().replace('_', ' ')


def format_lang_name(to_format: str):
    """
    Take a string representing the canonical name of a language (cpp, python, etc) and return its
    formatted name (C++, Python, etc). Any other string is converted to title case.

    :param to_format: the canonical language name
    :return: the formatted language name
    """
    code_entry = manifest_code.get(to_format)
    return code_entry.get('display') if code_entry else to_format.title().replace('_', ' ')


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


def get_num_algorithms():
    """
    :return: The number of algorithms
    """
    return len(get_all_algorithms())


def get_num_implementations():
    """
    :return: The total number of algorithm implementations
    """
    num_impl = 0
    for alg_info in manifest_algs.values():
        num_impl += len(alg_info.get('impl'))
    return num_impl


def get_num_languages():
    """
    :return: The number of languages
    """
    return len(get_all_languages())


def get_file_extension(language: str):
    """
    Get the file extension for a given language.

    :param language: the language
    :return: the corresponding file extension
    """
    return manifest_code.get(language).get('ext')


def homepage_markdown():
    """
    Read the contents of home.md and replace placeholders with appropriate values.

    :return: the main body of markdown for the home page
    """
    homepage_content = markdown_content(os.path.join(app_dir(), 'algs', 'home', 'home.md'))

    return homepage_content\
        .replace('{{{ num_alg }}}', str(get_num_algorithms()))\
        .replace('{{{ num_impl }}}', str(get_num_implementations()))\
        .replace('{{{ num_langs }}}', str(get_num_languages()))


def implementations(algorithm: str):
    """
    Get all languages with an implementation for the given algorithm

    :param algorithm: the algorithm
    :return: list of languages with an implementation for the given algorithm
    """
    return manifest_algs.get(algorithm).get('impl')


def markdown_content(path_to_file: str):
    """
    Return the contents of a file, or a string indicating the file could not be found.

    :param path_to_file:
    :return:
    """
    if os.path.isfile(path_to_file):
        return open(path_to_file, 'r').read().strip()
    else:
        return f'Cannot find file {path_to_file}'
