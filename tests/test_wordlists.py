# -*- coding: utf-8 -*-

from spoonerize.wordlists import DICTIONARY
from spoonerize.wordlists import STOPWORDS


#%% DICTIONARY

def test_dictionary():

    assert 'aardvark' in DICTIONARY
    assert 'zygote' in DICTIONARY


#%% STOPWORDS

def test_stopwords():

    assert 'the' in STOPWORDS
