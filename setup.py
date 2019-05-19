from setuptools import setup, find_packages

setup(
    name='wordgame',
    version='0.4.0',
    author='Aaron Robson',
    author_email='arobsonse@hotmail.co.uk',
    packages=find_packages(),
    url='https://github.com/AaronRobson/wordgame/',
    license='LICENSE.txt',
    description='A solver for wordgames such as scrabble and countdown.',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[],
    include_package_data=True,
    python_requires='>=3.6',
    zip_safe=False,
)
