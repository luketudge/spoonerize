# -*- coding: utf-8 -*-
"""Functions for finding spoonerisms in multi-word texts.
"""

from .regexes import VOWELS
from .regexes import WORD
from .word import strip_word


#%% Constants.

DEFAULT_MAX_DIST = 3


#%% Main function.

def spoonerize_text(text, maxdist=DEFAULT_MAX_DIST, stopwords=(), dictionary=None):
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
    (see :func:`is_spoonerizable_word`) ...
    * within ```max_dist`` word positions of each other ...
    * whose spoonerization results in two valid words \
    (see :func:`is_valid_word`).

    Each of the two words in a valid word pair \
    is returned as a tuple of *(start, end)*, \
    allowing the words to be sliced out \
    of the original input text.

    :param text: Text to search.
    :type text: str
    :param maxdist: Maximum permitted distance \
    between words in a pair.
    :type maxdist: int
    :return: Successive word pairs as *(start, end)* tuples.
    :rtype: iterator
    """

    pass

def is_spoonerizable_word(word, stopwords):
    """Check whether a word is spoonerizable.

    A spoonerizable word:

    * is not in ``stopwords`` ...
    * and contains at least three letters ...
    * at least one of which is a vowel.

    :param word: Word to check.
    :type word: str
    :param stopwords: Words to exclude.
    :type stopwords: iterable of str
    :rtype: bool
    """

    # Non-word characters.
    try:
        word = strip_word(word)[1]
    except ValueError:
        return False

    # Too short.
    if len(word) < 3:
        return False

    # Too few vowels.
    if all((v not in word) for v in VOWELS):
        return False

    # Stopword.
    if word.lower() in stopwords:
        return False

    return True


def is_valid_word(word, dictionary):
    """Check whether a word is valid.

    A valid word:

    * is in ``dictionary`` ...
    * or differs by one letter change \
    from a word in ``dictionary``.

    :param word: Word to check.
    :type word: str
    :param dictionary: Known words.
    :type dictionary: iterable of str
    :rtype: bool
    """

    pass
