# -*- coding: utf-8 -*-

from spoonerize.regexes import CV_BOUNDARY
from spoonerize.regexes import SENTENCE_BOUNDARY
from spoonerize.regexes import WORD


#%% SENTENCE_BOUNDARY

def test_sentence_boundary():

    # Period followed by whitespace.
    assert SENTENCE_BOUNDARY.split('a. b') == ['a', ' b']

    # Period followed by quotemark.
    assert SENTENCE_BOUNDARY.split('a." b') == ['a', '" b']

    # Period followed by string end.
    assert SENTENCE_BOUNDARY.split('a.') == ['a', '']

    # Exception word.
    assert SENTENCE_BOUNDARY.findall('dr. b') == []

    # Case insensitivity.
    assert SENTENCE_BOUNDARY.findall('Dr. b') == []

    # No boundary.
    assert SENTENCE_BOUNDARY.findall('a b') == []


#%% WORD

def test_word():

    for text in [' three. ', ' three 3 ', 'three']:
        assert WORD.findall(text) == ['three']

    for text in [' 3 ', ' se7en ', ' ... ', ' ', '']:
        assert WORD.findall(text) == []


#%% CV_BOUNDARY

def test_cv_boundary():

    # Standard case.
    assert CV_BOUNDARY.split('three', maxsplit=1) == ['thr', 'ee']

    # Starts with vowel.
    assert CV_BOUNDARY.split('our', maxsplit=1) == ['', 'our']

    # No vowel.
    assert CV_BOUNDARY.split('str', maxsplit=1) == ['str', '']

    # Case insensitivity.
    assert CV_BOUNDARY.split('Dear', maxsplit=1) == ['D', 'ear']
    assert CV_BOUNDARY.split('DEAR', maxsplit=1) == ['D', 'EAR']
