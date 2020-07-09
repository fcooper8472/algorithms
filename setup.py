from setuptools import setup

setup(
    name='algs',
    version='0.1',
    description='A compendium of algorithms and their implementations',
    url='https://github.com/fcooper8472/algorithms',
    author='Fergus Cooper',
    author_email='fergus.cooper@cs.ox.ac.uk',
    license='MIT',
    packages=['algs'],
    install_requires=[
        'altair',
        'numpy',
        'pandas',
        'pyyaml',
        'streamlit',
    ],
    extras_require={
        'dev': [
            'flake8',
            'pytest',
        ],
    },
    zip_safe=False
)
