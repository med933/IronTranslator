# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:14:50 2021

@author: M.ABDELMOULA
"""

import codecs
import os
import re
from setuptools import find_packages, setup

VERSION = '0.0.6'
DESCRIPTION = 'Google traduction'
LONG_DESCRIPTION = 'A package that allows to translate text.'

    
    
# Setting up
setup(
    name="IronTranslator",
    version=VERSION,
    author="Abdelmoula",
    author_email="abdelmoula.m93@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
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
                 'Programming Language :: Python :: 3.8']
)