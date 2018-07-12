""" Webdav for jianguoyun
See:
https://github.com/minjie-gu/scrat
"""

from setuptools import setup, find_packages
from codecs import open
from os import path
import scrat

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scrat',

    version=itchat.__version__,

    description='',
    long_description=long_description,

    url='https://github.com/minjie-gu/scrat',
    author='Minjie Gu',
    author_email='minjie_gu@126.com',
    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='webdav',

    packages=find_packages(),

    install_requires=['requests'],
    extras_require={},
)
