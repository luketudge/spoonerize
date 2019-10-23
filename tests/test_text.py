# -*- coding: utf-8 -*-

from spoonerize.text import find_valid_word_pairs
from spoonerize.text import is_spoonerizable_word
from spoonerize.text import is_valid_word


def test_find_valid_word_pairs():

    pass

def test_is_spoonerizable_word():

    # Positive case.
    assert is_spoonerizable_word('three', stopwords=())

    # Non-letter characters.
    assert not is_spoonerizable_word('se7en', stopwords=())

    # Too short.
    assert not is_spoonerizable_word('to', stopwords=())

    # No vowel.
    assert not is_spoonerizable_word('str', stopwords=())

def test_is_spoonerizable_word_stopwords():

    assert not is_spoonerizable_word('three', stopwords=('three',))
    assert not is_spoonerizable_word('Three', stopwords=('three',))

def test_is_valid_word():

    pass
