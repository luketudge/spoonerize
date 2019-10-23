# -*- coding: utf-8 -*-

import pytest

from spoonerize.word import copy_case_pattern
from spoonerize.word import split_word
from spoonerize.word import spoonerize_word_pair
from spoonerize.word import strip_word


def test_spoonerize_word_pair():

    examples = [('dear queen', 'quear deen'),
                ('loving shepherd', 'shoving lepherd'),
                ('crushing blow', 'blushing crow'),
                ('oiled bicycle', 'boiled icycle'),
                ('cosy nook', 'nosy cook')]

    for case, target in examples:
        assert spoonerize_word_pair(*case.split()) == tuple(target.split())

def test_spoonerize_word_pair_preserve_case():

    assert spoonerize_word_pair('dear', 'Queen') == ('quear', 'Deen')

def test_strip_word():

    # Standard case.
    assert strip_word(' three. ') == (' ', 'three', '. ')

    # No surroundings.
    assert strip_word('three') == ('', 'three', '')

def test_srip_word_error():

    with pytest.raises(ValueError):
        strip_word(' ... ')

def test_split_word():

    # Standard case.
    assert split_word('three') == ('thr', 'ee')

    # More than one c-v boundary.
    assert split_word('loving') == ('l', 'oving')

    # Starts with vowel.
    assert split_word('icicle') == ('', 'icicle')

def test_split_word_y():

    # As vowel.
    assert split_word('my') == ('m', 'y')

    # As consonant.
    assert split_word('your') == ('y', 'our')

def test_split_word_qu():

    # Standard case.
    assert split_word('queen') == ('qu', 'een')

    # 'qu' followed by consonant.
    assert split_word('quran') == ('q', 'uran')

    # 'q' without 'u'.
    assert split_word('qat') == ('q', 'at')

def test_split_word_error():

    for w in ('str', ' ', ''):
        with pytest.raises(ValueError):
            split_word(w)

def test_copy_case_pattern():

    # Use a test word with a non-standard case pattern.
    # This ensures that the function will change it.
    word = 'tHREE'

    # Lowercase.
    assert copy_case_pattern(word, 'cheers') == 'three'

    # Uppercase.
    assert copy_case_pattern(word, 'CHEERS') == 'THREE'

    # Capital.
    assert copy_case_pattern(word, 'Cheers') == 'Three'

def test_copy_case_pattern_whitespace():

    word = ' tHREE '

    # Lowercase.
    assert copy_case_pattern(word, ' cheers. ') == ' three '

    # Uppercase.
    assert copy_case_pattern(word, ' CHEERS. ') == ' THREE '

    # Capital.
    assert copy_case_pattern(word, ' Cheers. ') == ' Three '

def test_copy_case_pattern_edge_cases():

    word = 'tHREE'

    # Single uppercase letter.
    assert copy_case_pattern(word, 'A.') == 'THREE'
