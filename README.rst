IronTranslator: Google translate API for Python
===============================================

|PyPI latest| |PyPI License| |Stars|

Compatible with Python 3.6+.

1 - Installation
----------------

You can install it from PyPI.

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
  
.. |PyPI latest| image:: https://badge.fury.io/py/IronTranslator.svg
   :target: https://pypi.org/project/IronTranslator
.. |PyPI License| image:: https://img.shields.io/pypi/l/IronTranslator  
   :target: https://github.com/med933/IronTranslator/blob/main/LICENSE
.. |Stars| image:: https://img.shields.io/github/stars/med933/IronTranslator  
   :target: https://pypi.org/project/IronTranslator
