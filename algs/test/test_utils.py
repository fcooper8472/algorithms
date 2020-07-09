import algs
import os
import pytest


def test_app_dir():
    # check app_dir() returns a valid directory
    assert os.path.isdir(algs.app_dir())

    # check app_dir() contains the files algorithms.py (the main app) and setup.py
    assert os.path.isfile(os.path.join(algs.app_dir(), 'algorithms.py'))
    assert os.path.isfile(os.path.join(algs.app_dir(), 'setup.py'))


def test_manifest_algs():
    for alg in algs.manifest_algs.keys():
        # Check algorithm directory exists at the top level
        assert os.path.isdir(os.path.join(algs.app_dir(), 'algs', alg))

        # Check algorithm directory exists for each language it's implemented in
        for lang in algs.manifest_algs.get(alg).get('impl'):
            assert os.path.isdir(os.path.join(algs.app_dir(), 'code', lang, alg))

        # Check the display name matches the algorithm key
        assert algs.manifest_algs.get(alg).get('display').lower().replace(' ', '_') == alg


def test_manifest_code():
    for lang in algs.manifest_code.keys():
        lang_dir = os.path.join(algs.app_dir(), 'code', lang)
        lang_ext = algs.manifest_code.get(lang).get('ext')

        # Check lang directory exists
        assert os.path.isdir(lang_dir)

        # Check each stated algorithm directory & file exists
        for alg in algs.manifest_code.get(lang).get('impl'):
            assert os.path.isdir(os.path.join(lang_dir, alg))
            assert os.path.isfile(os.path.join(lang_dir, alg, f'{alg}.{lang_ext}'))


def test_manifests_agree():

    algs_from_algs = algs.manifest_algs.keys()
    langs_from_algs = set()
    for alg in algs_from_algs:
        langs_from_algs.update(algs.manifest_algs.get(alg).get('impl'))

    langs_from_langs = algs.manifest_code.keys()
    algs_from_langs = set()
    for lang in langs_from_langs:
        algs_from_langs.update(algs.manifest_code.get(lang).get('impl'))

    assert len(algs_from_algs) == len(algs_from_langs),\
        f'There are {len(algs_from_algs)} algorithms listed in manifest_algs.yaml but' \
        f' {len(algs_from_langs)} listed in manifest_code.yaml'

    assert len(langs_from_langs) == len(langs_from_algs),\
        f'There are {len(langs_from_langs)} languages listed in manifest_code.yaml but' \
        f' {len(langs_from_algs)} listed in manifest_algs.yaml'

    assert sorted(algs_from_algs) == sorted(list(algs_from_langs))
    assert sorted(langs_from_langs) == sorted(list(langs_from_algs))


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
