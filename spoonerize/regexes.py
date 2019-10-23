# -*- coding: utf-8 -*-
"""Regular expressions used in the other modules.

Regular expressions are compiled by the \
`regex <https://pypi.org/project/regex/>`_ package, \
with the ``V1`` flag set so as to allow splits at zero-width matches.
"""

import regex


FLAGS = regex.V1 | regex.IGNORECASE

# Word:
# word boundary
# followed by one or more word characters
# followed by word boundary
WORD = '\\b\\w+\\b'
WORD = regex.compile(WORD, flags=FLAGS)

# Letter types.
# 'y' is treated as a vowel here,
# but an exception is made later for 'y' at word start
# in the split_word() function.
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeéiïouy'

# Consonant-vowel (c-v) boundary:
# consonant or word boundary
# followed by vowel
CV_BOUNDARY = '(?<=\\b|[{}])(?=[{}])'.format(CONSONANTS, VOWELS)
CV_BOUNDARY = regex.compile(CV_BOUNDARY, flags=FLAGS)
