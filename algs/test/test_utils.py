import algs
import pytest


def test_app_dir():
    print(algs.app_dir())


def test_format_to_title():
    assert algs.format_to_title('hello_world') == 'Hello World'
    assert algs.format_to_title([]) == []
    assert algs.format_to_title(['a', 'a_b']) == ['A', 'A B']

    with pytest.raises(TypeError):
        algs.format_to_title(2)

