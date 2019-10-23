# -*- coding: utf-8 -*-

import regex


FLAGS = regex.V1 | regex.IGNORECASE

# Letter types.
# 'y' is treated as a vowel by default,
# but an exception is made later for 'y' at word start.
CONSONANTS = 'bcdfghjklmnpqrstvwxz'
VOWELS = 'aeéiïouy'

# Consonant-vowel (c-v) boundary:
# consonant or word boundary
# followed by vowel
CV_BOUNDARY = '(?<=\\b|[{}])(?=[{}])'.format(CONSONANTS, VOWELS)
CV_BOUNDARY = regex.compile(CV_BOUNDARY, flags=FLAGS)
