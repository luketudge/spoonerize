# -*- coding: utf-8 -*-
"""A streamlit app demonstrating the spoonerize package.
"""

import regex
import streamlit

import spoonerize
from spoonerize.wordlists import STOPWORDS, DICTIONARY


EXAMPLE_TEXT = "If you've had too many jelly beans you should take a shower."


#%% Helpers for highlighting changed words.

def mark_text(text):
    return '**' + text + '**'


def mark_changes(old, new):
    old_words = regex.split('\\b', old)
    new_words = regex.split('\\b', new)
    new_words_marked = [n if n == o else mark_text(n) for o, n in zip(old_words, new_words)]
    return ''.join(new_words_marked)


#%% Input text.

streamlit.title('spoonerisms!')

text = streamlit.text_area('Enter some text:', value=EXAMPLE_TEXT)


#%% Options sidebar.

if streamlit.sidebar.checkbox('valid dictionary words only', value=True):
    dictionary = DICTIONARY
else:
    dictionary = None

if streamlit.sidebar.checkbox('exclude stopwords (and, but, etc.)', value=True):
    stopwords = STOPWORDS
else:
    stopwords = ()

maxdist = streamlit.sidebar.radio('maximum distance between words', range(1, 6), index=1)


#%% Apply options and spoonerize.

text_out = spoonerize.spoonerize_text(
    text,
    maxdist=maxdist,
    stopwords=stopwords,
    dictionary=dictionary
)


#%% Output text.

streamlit.markdown(mark_changes(text, text_out))
