from algs import *

import os

import streamlit as st


algorithm_dropdown = st.sidebar.selectbox(
    label="Pick an algorithm:",
    options=get_all_algorithms(),
    format_func=format_alg_name
)

language_dropdown = st.sidebar.selectbox(
    label="Select a language:",
    options=implementations(algorithm_dropdown),
    format_func=format_lang_name
)

st.title(f'Algorithm: {format_alg_name(algorithm_dropdown)}')

md_file_name = f'{algorithm_dropdown}.md'

st.markdown(markdown_content(os.path.join(app_dir(), 'algs', algorithm_dropdown, md_file_name)))

st.subheader(f'{format_lang_name(language_dropdown)} implementation')


code_file_name = f'{algorithm_dropdown}.{get_file_extension(language_dropdown)}'
st.markdown(code_block(os.path.join(app_dir(), 'code', language_dropdown, algorithm_dropdown, code_file_name), language_dropdown))
