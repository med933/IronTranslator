# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:14:50 2021

@author: M.ABDELMOULA
"""

import codecs
import os.path
import re
from setuptools import find_packages, setup

VERSION = '0.1.4'
DESCRIPTION = 'Google traduction'
LONG_DESCRIPTION = 'A package that allows to translate text.'

def get_file(*paths):
    path = os.path.join(*paths)
    try:
        with open(path, 'rb') as f:
            return f.read().decode('utf8')
    except IOError:
        pass

def get_readme():
    return get_file(os.path.dirname(__file__), 'README.rst')


    
# Setting up
setup(
    name="IronTranslator",
    version=VERSION,
    license='MIT',
    author="Abdelmoula",
    author_email="abdelmoula.m93@gmail.com",
    description=DESCRIPTION,
    long_description_content_type='text/x-rst',
    packages=find_packages(),
    long_description=get_readme(),
    install_requires=['selenium','tqdm'],
    keywords=['python', 'Google traduction', 'traduction', 'nlp', 'Google', 'translate'],
    url='https://github.com/med933/IronTranslator',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Education',
                 'Intended Audience :: End Users/Desktop',
                 'License :: Freeware',
                 'Operating System :: POSIX',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: MacOS :: MacOS X',
                 'Topic :: Education',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 3.6',
                 'Programming Language :: Python :: 3.7',
                 'Programming Language :: Python :: 3.8'],
)



