# -*- coding: utf-8 -*-

from spoonerize.regexes import CV_BOUNDARY
from spoonerize.regexes import WORD


def test_word():

    for text in [' three. ', 'three']:
        assert WORD.findall(text) == ['three']

def test_word_edge_cases():

    for text in ['se7en', ' ... ', ' ', '']:
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
