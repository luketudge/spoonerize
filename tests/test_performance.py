# -*- coding: utf-8 -*-

import os
import timeit

from spoonerize import spoonerize_text
from spoonerize.wordlists import DICTIONARY
from spoonerize.wordlists import STOPWORDS


#%% Setup.

filename = 'melville-moby_dick.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
text = open(filepath, encoding='utf-8').read()

# Set a fairly generous time target
# (there are Windows users out there, too).
target = 10


#%% Functions to be called in timeit().

def no_wordlists():

    spoonerize_text(text)


def with_wordlists():

    spoonerize_text(text, stopwords=STOPWORDS, dictionary=DICTIONARY)


#%% Tests.

def test_speed_no_wordlists():

    t = timeit.timeit('no_wordlists()', number=1, globals=globals())
    assert t < target


def test_speed_with_wordlists():

    t = timeit.timeit('with_wordlists()', number=1, globals=globals())
    assert t < target
