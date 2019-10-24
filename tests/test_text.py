# -*- coding: utf-8 -*-

from spoonerize.text import find_next_sentence_boundary
from spoonerize.text import find_valid_word_pairs


#%% find_valid_word_pairs

def test_find_valid_word_pairs():

    pass


#%% find_next_sentence_boundary

def test_find_next_sentence_boundary():

    # Standard case.
    assert find_next_sentence_boundary('a. b') == 2

    # More than one boundary.
    assert find_next_sentence_boundary('a. b. c') == 2

    # No boundary.
    assert find_next_sentence_boundary('a b') is None

def test_find_next_sentence_boundary_exceptions():

    # Standard case.
    assert find_next_sentence_boundary('dr. b') is None

    # Uppercase.
    assert find_next_sentence_boundary('Dr. b') is None
