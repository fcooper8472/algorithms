from algs import *

import os

import streamlit as st


implemented_algorithms = get_implemented_algorithms()

algorithm_dropdown = st.sidebar.selectbox(
    label="Pick an algorithm:",
    options=get_all_algorithms(),
    format_func=format_to_title
)

language_dropdown = st.sidebar.selectbox(
    label="Select a language:",
    options=implemented_algorithms[algorithm_dropdown],
    format_func=format_to_lang
)

st.title(f'Algorithm: {algorithm_dropdown}')

selected_alg = format_from_title(algorithm_dropdown)
md_file_name = f'{selected_alg}.md'

st.markdown(markdown_content(os.path.join(app_dir(), 'algs', selected_alg, md_file_name)))

st.subheader(f'{language_dropdown} implementation')


selected_lang = format_from_lang(language_dropdown)
code_file_name = f'{selected_alg}.{get_file_extension(selected_lang)}'

st.markdown(code_block(os.path.join(app_dir(), 'code', selected_lang, selected_alg, code_file_name), selected_lang))
