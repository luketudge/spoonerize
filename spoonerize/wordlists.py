# -*- coding: utf-8 -*-
"""English wordlists.
"""

import os


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
DICTIONARY_FILE = os.path.join(DATA_PATH, 'dictionary.txt')
STOPWORDS_FILE = os.path.join(DATA_PATH, 'stopwords.txt')

DICTIONARY = open(DICTIONARY_FILE, encoding='utf-8').read().lower().split()
"""Dictionary of English words.

Source: `Unix words <https://en.wikipedia.org/wiki/Words_(Unix)>`_
"""

STOPWORDS = open(STOPWORDS_FILE, encoding='utf-8').read().split()
"""English stopwords.

Source: `nltk <https://github.com/nltk/nltk_data/blob/gh-pages/packages/corpora/stopwords.zip>`_
"""
