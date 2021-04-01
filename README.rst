IronTranslator: Google translate API for Python
===============================================

|PyPI latest| |PyPI License| |Stars|

IronTranslator is a simple tool to translate words or paragraphs with lengths less than 5000 words. IronTranslator may help you to do multiple tasks in nlp machine learning projects (in ordre to use GloVe or FastText).

Compatible with Python 3.6+.

1 - Installation
----------------

You can install it from `PyPI <https://pypi.org/project/IronTranslator/>`_.

.. code:: bash

   $ pip install IronTranslator

2 - How to use IronTranslator ?
-------------------------------

First you have to download the latest version of `ChromeDriver <https://chromedriver.chromium.org/>`_. Save the download file in the directory of your choice.

On Windows

.. code:: python

    >>> YourChromeDriverPath = r"C:\Users\chromedriver"
    
On Mac

.. code:: python

    >>> YourChromeDriverPath = "/Users/chromedriver"

Single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from IronTranslator import Translator
    >>> translator = Translator(ChromeDriverPath = YourChromeDriverPath)
    >>> translator.translate(texts=["bonjour"], dest='ko')
    100%|██████████████████████████████████████████████████| 1/1 [00:05<00:00,  0.70/it]
    ['안녕하세요']
    
Multiple sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   >>> from IronTranslator import Translator
   >>> translator = Translator(ChromeDriverPath = YourChromeDriverPath)
   >>> translator.translate(texts=["I Love Python.","The gravity on the moon's surface is 1.622 m / s2","What is the speed of light in a vacuum?"], dest='de')
   100%|██████████████████████████████████████████████████| 3/3 [00:05<00:00,  3.59s/it]
   ['Ich liebe Python.','Die Schwerkraft auf der Oberfläche des Mondes beträgt 1,622 m / s2',
   'Was ist die Lichtgeschwindigkeit im Vakuum?']
 
We can specify the source language 

.. code:: python

   >>> from IronTranslator import Translator
   >>> translator = Translator(ChromeDriverPath = YourChromeDriverPath)
   >>> translator.translate(texts=["I Love Real Madrid.","The gravity on the moon's surface is 1.622 m / s2",
                                   "What is the speed of light in a vacuum?"], dest='es',src='en')
   100%|██████████████████████████████████████████████████| 3/3 [00:05<00:00,  1.69s/it]
   ['Amo al Real Madrid.','La gravedad en la superficie de la luna es de 1.622 m / s2.','¿Cuál es la velocidad de la luz en un vacío?']

Available Languages :
-------------------------------

.. code:: python

   >>> {'afrikaans': 'af',
       'albanian': 'sq',
       'amharic': 'am',
       'arabic': 'ar',
       'armenian': 'hy',
       'azerbaijani': 'az',
       'basque': 'eu',
       'belarusian': 'be',
       'bengali': 'bn',
       'bosnian': 'bs',
       'bulgarian': 'bg',
       'catalan': 'ca',
       'cebuano': 'ceb',
       'chichewa': 'ny',
       'chinese (simplified)': 'zh-cn',
       'chinese (traditional)': 'zh-tw',
       'corsican': 'co',
       'croatian': 'hr',
       'czech': 'cs',
       'danish': 'da',
       'dutch': 'nl',
       'english': 'en',
       'esperanto': 'eo',
       'estonian': 'et',
       'filipino': 'tl',
       'finnish': 'fi',
       'french': 'fr',
       'frisian': 'fy',
       'galician': 'gl',
       'georgian': 'ka',
       'german': 'de',
       'greek': 'el',
       'gujarati': 'gu',
       'haitian creole': 'ht',
       'hausa': 'ha',
       'hawaiian': 'haw',
       'hebrew': 'he',
       'hindi': 'hi',
       'hmong': 'hmn',
       'hungarian': 'hu',
       'icelandic': 'is',
       'igbo': 'ig',
       'indonesian': 'id',
       'irish': 'ga',
       'italian': 'it',
       'japanese': 'ja',
       'javanese': 'jw',
       'kannada': 'kn',
       'kazakh': 'kk',
       'khmer': 'km',
       'korean': 'ko',
       'kurdish (kurmanji)': 'ku',
       'kyrgyz': 'ky',
       'lao': 'lo',
       'latin': 'la',
       'latvian': 'lv',
       'lithuanian': 'lt',
       'luxembourgish': 'lb',
       'macedonian': 'mk',
       'malagasy': 'mg',
       'malay': 'ms',
       'malayalam': 'ml',
       'maltese': 'mt',
       'maori': 'mi',
       'marathi': 'mr',
       'mongolian': 'mn',
       'myanmar (burmese)': 'my',
       'nepali': 'ne',
       'norwegian': 'no',
       'odia': 'or',
       'pashto': 'ps',
       'persian': 'fa',
       'polish': 'pl',
       'portuguese': 'pt',
       'punjabi': 'pa',
       'romanian': 'ro',
       'russian': 'ru',
       'samoan': 'sm',
       'scots gaelic': 'gd',
       'serbian': 'sr',
       'sesotho': 'st',
       'shona': 'sn',
       'sindhi': 'sd',
       'sinhala': 'si',
       'slovak': 'sk',
       'slovenian': 'sl',
       'somali': 'so',
       'spanish': 'es',
       'sundanese': 'su',
       'swahili': 'sw',
       'swedish': 'sv',
       'tajik': 'tg',
       'tamil': 'ta',
       'telugu': 'te',
       'thai': 'th',
       'turkish': 'tr',
       'ukrainian': 'uk',
       'urdu': 'ur',
       'uyghur': 'ug',
       'uzbek': 'uz',
       'vietnamese': 'vi',
       'welsh': 'cy',
       'xhosa': 'xh',
       'yiddish': 'yi',
       'yoruba': 'yo',
       'zulu': 'zu'}

.. |PyPI latest| image:: https://badge.fury.io/py/IronTranslator.svg
   :target: https://pypi.org/project/IronTranslator
.. |PyPI License| image:: https://img.shields.io/pypi/l/IronTranslator  
   :target: https://github.com/med933/IronTranslator/blob/main/LICENSE
.. |Stars| image:: https://img.shields.io/github/stars/med933/IronTranslator  
   :target: https://pypi.org/project/IronTranslator
