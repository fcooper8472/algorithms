from algs import *

import os

import streamlit as st


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

st.markdown(markdown_content(os.path.join(app_dir(), 'algs', selected_alg, md_file_name)))

st.subheader(f'{language_dropdown} implementation')


selected_lang = format_from_lang(language_dropdown)
code_file_name = f'{selected_alg}.{get_file_extension(selected_lang)}'

st.markdown(code_block(os.path.join(app_dir(), 'code', selected_lang, selected_alg, code_file_name), selected_lang))
