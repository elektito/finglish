Finglish to Persian Converter
=============================

This library provides a Finglish-to-Persian convertor.

::

    >>> from finglish import f2p
    >>> f2p('asemane abi')
    'آسمان آبی'

(Your browser might be showing some garbled text due to the presence
of Persian text. Try this in Python shell with a Unicode-aware
Terminal.)

The return value is a list of possibilities, each with a confidence
value in the [0.0, 1.0] range.
