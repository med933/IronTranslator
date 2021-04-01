===============================================================
IronTranslator: Google translate API for Python
===============================================================

|PyPI Versio|

----------
Installation
----------
You can install it from PyPI.
.. sourcecode:: bash

   $ pip install IronTranslator

..
----------
How to use IronTranslator ?
----------

First you have to download the latest version of `ChromeDriver <https://chromedriver.chromium.org/>`_. Save the download file in the directory of your choice.

.. code:: python

    >>> YourChromeDriverPath = r"C:\Users\chromedriver"
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from IronTranslator import Translator
    >>> translator = Translator(ChromeDriverPath = YourChromeDriverPath)
    >>> translator.translate(texts=["bonjour"], dest='ko')
    ['안녕하세요']
    
