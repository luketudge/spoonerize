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


def test_spoonerize_word_pair_context():

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

    text = '''Three cheers for our dear old queen!
    The Lord is a loving shepherd.
    A crushing blow.
    A well-oiled bicycle.
    You were lighting a fire in the quadrangle.
    Is the dean busy?
    Please show me to another seat.
    You have missed all my history lectures.
    You have wasted a whole term.
    '''

    target = '''Three cheers for our quear old deen!
    The Lord is a shoving lepherd.
    A blushing crow.
    A well-boiled icycle.
    You were fighting a lire in the quadrangle.
    Is the bean dusy?
    Please sow me to another sheat.
    You have hissed all my mistory lectures.
    You have tasted a whole werm.
    '''

    stopwords = ('a',
                 'all',
                 'another',
                 'for',
                 'have',
                 'in',
                 'is',
                 'me',
                 'my',
                 'our',
                 'the',
                 'to',
                 'were',
                 'whole',
                 'you')

    dictionary = ('bean',
                  'blushing',
                  'boiled',
                  'crow',
                  'deen',
                  'dusy',
                  'fighting',
                  'hissed',
                  'icycle',
                  'lepherd',
                  'lire',
                  'mistory',
                  'quear',
                  'sheat',
                  'shoving',
                  'sow',
                  'tasted',
                  'werm')

    result = spoonerize_text(text, maxdist=4,
                             stopwords=stopwords,
                             dictionary=dictionary)
    assert result == target
