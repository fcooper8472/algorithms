import algs
import os
import pytest


def test_app_dir():
    # check app_dir() returns a valid directory
    assert os.path.isdir(algs.app_dir())

    # check app_dir() contains the files algorithms.py (the main app) and setup.py
    assert os.path.isfile(os.path.join(algs.app_dir(), 'algorithms.py'))
    assert os.path.isfile(os.path.join(algs.app_dir(), 'setup.py'))


def test_code_block():
    # check behaviour with known file
    known_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_code_block.hpp')
    expected_block_lang = '```cpp\nint main() {\n    return 0;\n}\n```'
    expected_block_bare = '```\nint main() {\n    return 0;\n}\n```'
    assert algs.code_block(known_file, 'cpp') == expected_block_lang
    assert algs.code_block(known_file) == expected_block_bare

    # check behaviour with invalid file
    assert algs.code_block('/path/to/fake/file') == 'Cannot find file /path/to/fake/file'


def test_format_to_title():
    assert algs.format_to_title('hello_world') == 'Hello World'
    assert algs.format_to_title([]) == []
    assert algs.format_to_title(['a', 'a_b']) == ['A', 'A B']

    with pytest.raises(TypeError):
        algs.format_to_title(2)
