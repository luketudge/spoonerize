# -*- coding: utf-8 -*-

from spoonerize.wordlists import DICTIONARY
from spoonerize.wordlists import STOPWORDS


#%% DICTIONARY

def test_dictionary():

    assert 'aardvark' in DICTIONARY
    assert 'zygote' in DICTIONARY


def test_dictionary_variants():

    # Plurals.
    assert 'aardvarks' in DICTIONARY

    # Conjugations.
    for suffix in ['s', 'ed', 'ing']:
        assert 'abandon' + suffix in DICTIONARY

    # Regional variants.
    assert 'accessorise' in DICTIONARY
    assert 'accessorize' in DICTIONARY


#%% STOPWORDS

def test_stopwords():

    assert 'the' in STOPWORDS
