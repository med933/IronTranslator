# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 23:14:50 2021

@author: M.ABDELMOULA
"""

import codecs
import os
import re
from setuptools import find_packages, setup

VERSION = '0.0.2'
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
    install_requires=['selenium', 'pandas', 'BeautifulSoup','tqdm'],
    keywords=['python', 'Google traduction', 'traduction', 'nlp', 'Google'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)