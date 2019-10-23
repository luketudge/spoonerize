# -*- coding: utf-8 -*-

from spoonerize.regexes import CV_BOUNDARY
from spoonerize.regexes import WORD


def test_word():

    for case in [' three. ', 'three']:
        assert WORD.findall(case) == ['three']

def test_word_edge_cases():

    for case in [' ... ', ' ', '']:
        assert WORD.findall(case) == []

def test_cv_boundary():

    # Standard case.
    assert CV_BOUNDARY.split('three') == ['thr', 'ee']

    # Starts with vowel.
    assert CV_BOUNDARY.split('icicle', maxsplit=1) == ['', 'icicle']

def test_cv_boundary_case_sensitivity():

    assert CV_BOUNDARY.split('Dear') == ['D', 'ear']
    assert CV_BOUNDARY.split('DEAR') == ['D', 'EAR']

def test_cv_boundary_whitespace():

    assert CV_BOUNDARY.split(' three') == [' thr', 'ee']
    assert CV_BOUNDARY.split(' icicle', maxsplit=1) == [' ', 'icicle']

def test_cv_boundary_edge_cases():

    # No boundary.
    assert CV_BOUNDARY.split('str') == ['str']

    # Empty.
    assert CV_BOUNDARY.split(' ') == [' ']
    assert CV_BOUNDARY.split('') == ['']
