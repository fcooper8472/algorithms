import os
import streamlit


def main():
    """
    A nasty hack to add Google Analytics (until Streamlit allows adding custom JS or HTML).
    Edit the static index.html in the streamlit module.
    """

    streamlit_dir = os.path.dirname(streamlit.__file__)
    index_html = os.path.join(streamlit_dir, 'static', 'index.html')

    if not os.path.isfile(index_html):
        return

    analytics_code = """<head><script async src="https://www.googletagmanager.com/gtag/js?id=UA-140848718-3"></script><script>window.dataLayer=window.dataLayer || []; function gtag(){dataLayer.push(arguments);}gtag('js', new Date()); gtag('config', 'UA-140848718-3');</script>"""

    original_content = open(index_html, 'r').read()

    if 'UA-140848718-3' not in original_content:
        with open(index_html, 'w') as f:
            f.write(original_content.replace('<head>', analytics_code))


if __name__ == '__main__':
    main()
