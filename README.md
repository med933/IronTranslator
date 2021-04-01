

IronTranslator: Free Google translate API for Python

python 3.6+

----------
Installation
----------
You can install it from PyPI:

.. sourcecode:: bash

   $ pip install IronTranslator


~~~~~~~~~~~~~~~~~~~~~~~~~~~
single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

    >>> from GoogleFreeTrans import Translator
    >>> translator = Translator.translator(src='en', dest='fr')
    >>> translator.translate('china')
    'Chine'

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
multiple sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: python

   >>> from GoogleFreeTrans import Translator
   >>> translator = Translator.translator(src='en', dest='fr')
   >>> translator.translate('china. french')
   [[['Chine. ', 'china.', None, None, 1],  ['français.', 'french.', None, None, 1]], None, 'en']
