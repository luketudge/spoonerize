# -*- coding: utf-8 -*-

from spoonerize.regexes import CV_BOUNDARY
from spoonerize.regexes import SENTENCE_BOUNDARY
from spoonerize.regexes import WORD


def test_sentence_boundary():

    # Period followed by whitespace.
    assert SENTENCE_BOUNDARY.split('a. b') == ['a.', ' b']

    # Period followed by quotemark.
    assert SENTENCE_BOUNDARY.split('a." b') == ['a.', '" b']

    # Period followed by string end.
    assert SENTENCE_BOUNDARY.split('a.') == ['a.', '']

    # No boundary.
    assert SENTENCE_BOUNDARY.findall('a b') == []

def test_word():

    for text in [' three. ', ' three 3 ', 'three']:
        assert WORD.findall(text) == ['three']

def test_word_nonwords():

    for text in [' 3 ', ' se7en ', ' ... ', ' ', '']:
        assert WORD.findall(text) == []

def test_cv_boundary():

    # Standard case.
    assert CV_BOUNDARY.split('three', maxsplit=1) == ['thr', 'ee']

    # Starts with vowel.
    assert CV_BOUNDARY.split('our', maxsplit=1) == ['', 'our']

    # No vowel.
    assert CV_BOUNDARY.split('str', maxsplit=1) == ['str', '']

def test_cv_boundary_case_sensitivity():

    assert CV_BOUNDARY.split('Dear', maxsplit=1) == ['D', 'ear']
    assert CV_BOUNDARY.split('DEAR', maxsplit=1) == ['D', 'EAR']
