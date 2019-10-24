# -*- coding: utf-8 -*-
"""Regular expressions used in the other modules.

Regular expressions are compiled by the \
`regex <https://pypi.org/project/regex/>`_ package, \
with the ``V1`` flag set so as to allow splits at zero-width matches.
"""

import regex


FLAGS = regex.V1 | regex.IGNORECASE

SENTENCE_STOPS = '.?!:;'
"""Sentence stop characters.
"""

QUOTEMARKS = ''''"’”'''
"""'Closing' quote characters.
"""

SENTENCE_BOUNDARY = '(?<=[{}])(?=\\s|[{}]|$)'.format(SENTENCE_STOPS, QUOTEMARKS)
SENTENCE_BOUNDARY = regex.compile(SENTENCE_BOUNDARY, flags=FLAGS)
"""Regular expression for sentence boundary.

* Any of :data:`SENTENCE_STOPS` ...
* followed by any of  :data:`QUOTEMARKS` ...
* or whitespace ...
* or string end.
"""

CONSONANTS = 'bcdfghjklmnpqrstvwxz'
"""Consonants.
"""

VOWELS = 'aeéiïouy'
"""Vowels.

`'y'` is treated as a vowel by default, \
but an exception is made in :func:`.word.split_word` \
for `'y'` at the start of a word.
"""

WORD = '\\b[{}{}]+\\b'.format(CONSONANTS, VOWELS)
WORD = regex.compile(WORD, flags=FLAGS)
"""Regular expression for a word.

Uses an explicit set of letter characters \
instead of the regular expression word character ``'\\w'``. \
This allows excluding digits \
and characters from unsupported languages.
"""

CV_BOUNDARY = '(?<=^|[{}])(?=[{}]|$)'.format(CONSONANTS, VOWELS)
CV_BOUNDARY = regex.compile(CV_BOUNDARY, flags=FLAGS)
"""Consonant-vowel (*c-v*) boundary.

Used in :func:`.word.split_word`.
"""
