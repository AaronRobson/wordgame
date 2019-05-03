from setuptools import setup

setup(
    name='wordgame',
    version='0.1.0',
    author='Aaron Robson',
    author_email='aaronrse@hotmail.co.uk',
    packages=['wordgame', 'wordgame.test'],
    url='http://pypi.python.org/pypi/wordplay/',
    license='LICENSE.txt',
    description='A solver for wordgames such as scrabble and countdown.',
    long_description=open('README.md').read(),
    install_requires=[],
    include_package_data=True,
)
