# -*- coding: utf-8 -*-
"""English wordlists.
"""

import os


DATA_PATH = os.path.join(os.path.dirname(__file__), 'data')
DICTIONARY_FILE = os.path.join(DATA_PATH, 'dictionary.txt')
STOPWORDS_FILE = os.path.join(DATA_PATH, 'stopwords.txt')

DICTIONARY = open(DICTIONARY_FILE, encoding='utf-8').read()
DICTIONARY = set(DICTIONARY.lower().split())
"""Dictionary of English words.

Source: `SCOWL <https://github.com/en-wl/wordlist>`_
"""

STOPWORDS = open(STOPWORDS_FILE, encoding='utf-8').read()
STOPWORDS = set(STOPWORDS.lower().split())
"""English stopwords.

Source: `nltk <https://github.com/nltk/nltk_data/blob/gh-pages/packages/corpora/stopwords.zip>`_
"""
