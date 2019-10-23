# -*- coding: utf-8 -*-
"""Functions for spoonerizing word pairs.
"""

from .regexes import CV_BOUNDARY
from .regexes import VOWELS
from .regexes import WORD


#%% Main function.

def spoonerize_word_pair(word1, word2):
    """Spoonerize a word pair.

    Words are spoonerized by exchanging their *heads* \
    (see :func:`split_word`).

    The *case pattern* of the original words is preserved \
    (see :func:`copy_case_pattern`).

    :param word1: First word.
    :type word1: str
    :param word2: Second word.
    :type word2: str
    :return: Spoonerized words.
    :rtype: tuple (str, str)
    """

    head1, body1 = split_word(word1)
    head2, body2 = split_word(word2)

    word1_new = head2 + body1
    word2_new = head1 + body2

    word1_new = copy_case_pattern(word1_new, word1)
    word2_new = copy_case_pattern(word2_new, word2)

    return word1_new, word2_new


#%% Helper functions.

def strip_word(text):
    """Separate a word from its surroundings.

    The first word in ``text`` is extracted according to the \
    'word character' regular expression ``'\\w'``, \
    and returned along with any non-word characters \
    to its left and right. \
    Any additional words in ``text`` are treated as \
    part of the *right* surroundings of the word.

    :param text: Text containing a word to extract.
    :type text: str
    :return: *left*, *word*, *right*
    :rtype: tuple (str, str, str)
    """

    match = WORD.search(text)

    if match is None:
        raise ValueError("No word found in '{}'.".format(text))

    start = match.start()
    end = match.end()

    return text[:start], text[start:end], text[end:]

def split_word(word):
    """Split a word into head and body.

    The *head* of a word is the first consonant cluster \
    up to but not including the first vowel. \
    The *body* is the remainder of the word. \
    Words that begin with a vowel have an empty head.

    ``'y'`` is treated as a vowel, \
    except at the beginning of a word. \
    If the letter combination ``'qu'``, \
    is followed by a vowel, \
    the ``'qu'`` is treated as a consonant.

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

    components = CV_BOUNDARY.split(word, maxsplit=1)

    if len(components) == 1:
        raise ValueError("No c-v boundary found in '{}'.".format(word))

    head, body = components

    # Exception: Initial 'y' as consonant.
    if (not head[-1:].isalpha()) and body.lower().startswith('y'):
        head = head + body[0]
        body = body[1:]

    # Exception: 'qu'.
    elif head.lower().endswith('q') and body.lower().startswith('u'):
        if body[1:2] and (body[1:2].lower() in VOWELS):
            head = head + body[0]
            body = body[1:]

    return head, body

def copy_case_pattern(word, model):
    """Apply the *case pattern* of one word to another.

    Three case patterns are recognized:

    * *lowercase*: The first letter is lowercase.
    * *uppercase*: All letters are uppercase.
    * *capital*: the first letter is uppercase, \
    and at least one other letter is lowercase.

    The case pattern detected for ``model`` \
    is applied to ``word`` using:

    * *lowercase*: ``str.lower()``
    * *uppercase*: ``str.upper()``
    * *capital*: ``str.capitalize()``

    :param word: Word to transform.
    :type word: str
    :param model: Word whose case pattern is to be copied.
    :type model: str
    :return: ``word`` in case pattern of ``model``.
    :rtype: str
    """

    left, word, right = strip_word(word)
    model = strip_word(model)[1]

    # Lowercase.
    if model[:1].islower():
        word = word.lower()

    # Uppercase.
    elif model.isupper():
        word = word.upper()

    # Capital.
    else:
        word = word.capitalize()

    return left + word + right
