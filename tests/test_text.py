# -*- coding: utf-8 -*-

from spoonerize.text import find_valid_word_pairs


#%% find_valid_word_pairs

def test_find_valid_word_pairs():

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text))
    assert len(pairs) == 2
    assert pairs[0] == ((0, 4, 'Quear'), (5, 10, 'deen'))
    assert pairs[1] == ((14, 20, 'shoving'), (21, 29, 'lepherd'))

def test_find_valid_word_pairs_maxdist():

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text, maxdist=0))
    assert pairs == []

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text, maxdist=4,
                                       stopwords=('queen', 'loving')))
    assert len(pairs) == 1
    assert pairs[0] == ((0, 4, 'Shear'), (21, 29, 'depherd'))

def test_find_valid_word_pairs_stopwords():

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text,
                                       stopwords=('loving',)))
    assert len(pairs) == 1
    assert pairs[0] == ((0, 4, 'Quear'), (5, 10, 'deen'))

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text, maxdist=2,
                                       stopwords=('dear', 'shepherd')))
    assert len(pairs) == 1
    assert pairs[0] == ((5, 10, 'leen'), (14, 20, 'quoving'))

def test_find_valid_word_pairs_dictionary():

    text = 'Dear queen, a loving shepherd'
    pairs = list(find_valid_word_pairs(text,
                                       dictionary=('quear', 'deen')))
    assert len(pairs) == 1
    assert pairs[0] == ((0, 4, 'Quear'), (5, 10, 'deen'))

def test_find_valid_word_pairs_sentence_boundary():

    text = 'Dear queen. A loving shepherd'
    pairs = list(find_valid_word_pairs(text, maxdist=2,
                                       stopwords=('dear', 'shepherd')))
    assert pairs == []

def test_find_valid_word_pairs_edge_cases():

    for text in [' ... ', ' ', '', 'se7en']:
        assert list(find_valid_word_pairs(text)) == []
