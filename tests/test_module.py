# -*- coding: utf-8 -*-

from spoonerize import spoonerize_text
from spoonerize import spoonerize_word_pair


#%% spoonerize_word_pair

examples = [(('dear', 'queen'), ('quear', 'deen')),
            (('loving', 'shepherd'), ('shoving', 'lepherd')),
            (('crushing', 'blow'), ('blushing', 'crow')),
            (('oiled', 'bicycle'), ('boiled', 'icycle')),
            (('cosy', 'nook'), ('nosy', 'cook'))]

def test_spoonerize_word_pair():

    for pair, target in examples:
        assert spoonerize_word_pair(*pair) == target

def test_spoonerize_word_pair_strip():

    assert spoonerize_word_pair('-dear ', 'queen.') == ('-quear ', 'deen.')

def test_spoonerize_word_pair_preserve_case():

    # Lower, upper.
    assert spoonerize_word_pair('dear', 'QUEEN') == ('quear', 'DEEN')

    # Lower, capital.
    assert spoonerize_word_pair('dear', 'Queen') == ('quear', 'Deen')

    # Upper, lower.
    assert spoonerize_word_pair('DEAR', 'queen') == ('QUEAR', 'deen')

    # Upper, capital.
    assert spoonerize_word_pair('DEAR', 'Queen') == ('QUEAR', 'Deen')

    # Capital, lower.
    assert spoonerize_word_pair('Dear', 'queen') == ('Quear', 'deen')

    # Capital, upper.
    assert spoonerize_word_pair('Dear', 'QUEEN') == ('Quear', 'DEEN')


#%% spoonerize_text

def test_spoonerize_text():

    pass
