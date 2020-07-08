import algs
import os

import streamlit as st

from typing import Iterable, Union


def format_to_title(to_format: Union[Iterable[str], str]):
    if isinstance(to_format, str):
        return to_format.title().replace('_', ' ')
    else:
        return [format_to_title(x) for x in to_format]


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


def format_from_lang(to_format: Union[Iterable[str], str]):
    if isinstance(to_format, str):
        if to_format == 'C++':
            return 'cpp'
        else:
            return to_format.lower()
    else:
        return [format_from_lang(x) for x in to_format]


def get_file_extension(language: str):
    extension_lookup = {
        'cpp': 'hpp',
        'julia': 'jl',
        'python': 'py',
        'rust': 'rs',
    }
    return extension_lookup[language]


def script_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_all_languages():
    lang_dirs = os.listdir(os.path.join(script_dir(), 'code'))
    return sorted([lang for lang in lang_dirs if os.path.isdir(os.path.join(script_dir(), 'code', lang))])


def get_all_algorithms():
    alg_dirs = [x for x in os.listdir(os.path.join(script_dir(), 'algs')) if not x.startswith('_')]
    return sorted([alg for alg in alg_dirs if os.path.isdir(os.path.join(script_dir(), 'algs', alg))])


def get_implemented_algorithms():
    algs = {}
    for alg in get_all_algorithms():
        algs[alg] = []
        for lang in get_all_languages():
            if os.path.isdir(os.path.join(script_dir(), 'code', lang, alg)):
                algs[alg].append(lang)
    return algs


def code_block(path_to_file, markdown_lang=''):
    if os.path.isfile(path_to_file):
        file_content = open(path_to_file, 'r').read().strip()
        return f"```{markdown_lang}\n{file_content}\n```"
    else:
        return f'Cannot find file {path_to_file}'


def markdown_content(path_to_file):
    if os.path.isfile(path_to_file):
        return open(path_to_file, 'r').read().strip()
    else:
        return f'Cannot find file {path_to_file}'


implemented_algorithms = get_implemented_algorithms()

algorithm_dropdown = st.sidebar.selectbox(
    "Pick an algorithm:",
    format_to_title(get_all_algorithms())
)

language_dropdown = st.sidebar.selectbox(
    "Select a language:",
    format_to_title(format_to_lang(implemented_algorithms[format_from_title(algorithm_dropdown)]))
)

st.title(f'Algorithm: {algorithm_dropdown}')

selected_alg = format_from_title(algorithm_dropdown)
md_file_name = f'{selected_alg}.md'

st.markdown(markdown_content(os.path.join(script_dir(), 'algs', selected_alg, md_file_name)))

st.subheader(f'{language_dropdown} implementation')


selected_lang = format_from_lang(language_dropdown)
code_file_name = f'{selected_alg}.{get_file_extension(selected_lang)}'

st.markdown(code_block(os.path.join(script_dir(), 'code', selected_lang, selected_alg, code_file_name), selected_lang))

st.title(algs.greet("World"))
