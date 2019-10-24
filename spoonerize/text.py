# -*- coding: utf-8 -*-
"""Functions for finding spoonerisms in multi-word texts.
"""

from .regexes import SENTENCE_BOUNDARY
from .regexes import SENTENCE_BOUNDARY_EXCEPTIONS
from .regexes import VOWELS
from .regexes import WORD
from .word import is_spoonerizable_word
from .word import is_valid_word
from .word import strip_word


#%% Main function.

def spoonerize_text(text, maxdist=3, stopwords=(), dictionary=None):
    """Spoonerize all valid word pairs in a text.

    All valid word pairs in ``text`` are spoonerized \
    (see :func:`find_valid_word_pairs` \
    for an explanation of valid word pairs).

    :param text: Text to spoonerize.
    :type text: str
    :param maxdist: Passed on to :func:`find_valid_word_pairs`
    :type maxdist: int
    :param stopwords: Passed on to :func:`is_spoonerizable_word`
    :type stopwords: iterable of str
    :param dictionary: Passed on to :func:`is_valid_word`
    :type dictionary: iterable of str
    :return: Spoonerized text.
    :rtype: str
    """

    pass


#%% Helper functions.

def find_valid_word_pairs(text, maxdist):
    """Find valid word pairs in a text.

    A valid word pair:

    * consists of two *spoonerizable* words \
    (see :func:`.word.is_spoonerizable_word`) ...
    * within ``max_dist`` word positions of each other ...
    * that do not span a sentence boundary \
    (see :data:`.regexes.SENTENCE_BOUNDARY`), ...
    * and whose spoonerization results in two valid words \
    (see :func:`.word.is_valid_word`).

    Each of the two words in a valid word pair \
    is returned as a tuple of *(start, end)*, \
    allowing the words to be sliced out \
    of the original input text.

    :param text: Text to search.
    :type text: str
    :param maxdist: Maximum permitted distance \
    between words.
    :type maxdist: int
    :return: Successive word pairs as *(start, end)* tuples.
    :rtype: iterator
    """

    pass

def find_next_sentence_boundary(text):
    """Find the position of the next sentence boundary in a text.

    See :data:`.regexes.SENTENCE_BOUNDARY`.

    If no boundary is found, return ``None``.

    :param text: Text in which to search.
    :type text: str
    :return: Position of first sentence boundary.
    :rtype: int
    """

    match = SENTENCE_BOUNDARY.search(text)

    if match is None:
        return None

    return match.end()
