# -*- coding: utf-8 -*-
"""Functions for spoonerizing word pairs.
"""

from .regexes import CV_BOUNDARY
from .regexes import VOWELS


def split_word(word):
    """Split a word into head and body.

    The *head* of a word is the first consonant cluster \
    up to but not including the first vowel, \
    and the *body* is the remainder of the word. \
    Words that begin with a vowel have an empty head.

    *y* is treated as a vowel, \
    except at the beginning of a word. \
    In the letter combination *qu<VOWEL>*, \
    *qu* is treated as a consonant.

    If ``word`` contains multiple words, \
    only the first word is split. \
    Remaining words are included in the body.

    :param word: Word to split.
    :type word: str
    :return: head and body
    :rtype: tuple (str, str)
    :raises ValueError: If ``word`` \
    contains no boundary at which to split.
    """

    try:
        head, body = CV_BOUNDARY.split(word, maxsplit=1)
    except ValueError:
        raise ValueError("No split boundary found in '{}'.".format(word))

    # Exception: Initial 'y' as consonant.
    if (not head[-1:].isalpha()) and body.lower().startswith('y'):
        head = head + body[0]
        body = body[1:]

    # Exception: 'qu'.
    if head.lower().endswith('q') and body.lower().startswith('u'):
        if body[1:2] and (body[1:2] in VOWELS):
            head = head + body[0]
            body = body[1:]

    return head, body

def spoonerize_word_pair(word1, word2):
    """Spoonerize a word pair.

    Words are spoonerized by exchanging their *heads* \
    (see :func:`split_word` for an explanation of word heads).

    :param word1: First word.
    :type word1: str
    :param word2: Second word.
    :type word2: str
    :return: Spoonerized words.
    :rtype: tuple (str, str)
    """

    head1, body1 = split_word(word1)
    head2, body2 = split_word(word2)

    return head2+body1, head1+body2
