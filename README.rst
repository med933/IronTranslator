===============================================================
IronTranslator: Google translate API for Python
===============================================================

|PyPI Versio|

----------
1 - Installation
----------
You can install it from PyPI.
.. sourcecode:: bash

   $ pip install IronTranslator

..
----------
2 - How to use IronTranslator ?
----------

First you have to download the latest version of `ChromeDriver <https://chromedriver.chromium.org/>`_. Save the download file in the directory of your choice.

---
On Windows
---

.. code:: python

    >>> YourChromeDriverPath = r"C:\Users\chromedriver"
    
---
On Mac
---

.. code:: python

    >>> YourChromeDriverPath = "/Users/chromedriver"
~~~~~~~~~~~~~~~~~~~~~~~~~~~
Single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from IronTranslator import Translator
    >>> translator = Translator(ChromeDriverPath = YourChromeDriverPath)
    >>> translator.translate(texts=["bonjour"], dest='ko')
    ['안녕하세요']
    
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Multiple sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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
   
   
   
   
   
