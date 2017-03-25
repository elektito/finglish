Finglish to Persian Converter
=============================

This library provides a Finglish-to-Persian convertor.

::

    >>> from finglish import f2p
    >>> f2p('man va to')
    [('آسمان آبی', 1.0), ('عثمان آبی', 0.32267613972764947), ('آسمان ابی', 0.2849966510381782), ('عثمان ابی', 0.09196161919230733), ('اسمان آبی', 0.008288928359976317), ('اسمان ابی', 0.002362316823288629), ('آسمان عبی', 0.0006697923643670462), ('عثمان عبی', 0.0002161260145530137), ('اسمان عبی', 5.5518609242976e-06)]

(Your browser might be showing some garbled text due to the presence of
Persian text. Try this in Python shell.)

The return value is a list of possibilities, each with a confidence
value in the [0.0, 1.0] range.
