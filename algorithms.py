from algs import *

import os

import streamlit as st

placeholder = 'Select...'

st.sidebar.title(f'The Algorithm Zoo')
home_button = st.sidebar.button('Home')

alg_dd = st.sidebar.selectbox(
    label="Pick an algorithm:",
    options=[placeholder] + get_all_algorithms(),
    format_func=format_alg_name
)

if alg_dd == 'Select...' or home_button:
    st.title(f'The Algorithm Zoo')
    st.markdown(homepage_markdown())
else:
    language_dropdown = st.sidebar.selectbox(
        label="Select a language:",
        options=implementations(alg_dd),
        format_func=format_lang_name
    )

    st.title(f'Algorithm: {format_alg_name(alg_dd)}')

    # Markdown description of the algorithm, in algs/<algorithm>/<algorithm>.md
    md_file_name = f'{alg_dd}.md'
    st.markdown(markdown_content(os.path.join(app_dir(), 'algs', alg_dd, md_file_name)))

    # Interactive examples/visualisation, in algs/<algorithm>/__init__.py
    display_alg_content(alg_dd)

    # Implementation of algorithm in specified language
    st.subheader(f'{format_lang_name(language_dropdown)} implementation')
    code_file_name = f'{alg_dd}.{get_file_extension(language_dropdown)}'
    path_to_code = os.path.join(app_dir(), 'code', language_dropdown, alg_dd, code_file_name)
    st.markdown(code_block(path_to_code, language_dropdown))
