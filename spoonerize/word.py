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

    # Strip from surroundings.
    left1, word1, right1 = strip_word(word1)
    left2, word2, right2 = strip_word(word2)

    # Split.
    head1, body1 = split_word(word1)
    head2, body2 = split_word(word2)

    # Spoonerize
    word1_new = head2 + body1
    word2_new = head1 + body2

    # Preserve case pattern.
    word1_new = copy_case_pattern(word1_new, word1)
    word2_new = copy_case_pattern(word2_new, word2)

    # Reunite with surroundings.
    word1_new = left1 + word1_new + right1
    word2_new = left2 + word2_new + right2

    return word1_new, word2_new


#%% Helper functions.

def strip_word(text):
    """Separate a word from its surroundings.

    The first word is extracted from ``text`` \
    using :data:`.regexes.WORD` \
    and separated from any other characters \
    to its left and right.

    ``strip_word`` is applied to the string arguments \
    of the following functions \
    in order to deal flexibly with words in context:

    * :func:`copy_case_pattern`
    * :func:`is_spoonerizable_word`
    * :func:`is_valid_word`
    * :func:`split_word`
    * :func:`spoonerize_word_pair`

    :param text: Text containing a word.
    :type text: str
    :return: Word and surroundings as \
    (*left*, *word*, *right*).
    :rtype: tuple (str, str, str)
    :raises ValueError: If ``text`` does not contain a word.
    """

    match = WORD.search(text)

    if match is None:
        raise ValueError("No word found in '{}'.".format(text))

    start, end = match.span()

    return text[:start], text[start:end], text[end:]


def is_spoonerizable_word(word, stopwords=()):
    """Check whether a word is spoonerizable.

    A spoonerizable word:

    * is not in ``stopwords``, ...
    * contains only letter characters, ...
    * and contains at least three letters ...
    * at least one of which is a vowel.

    :param word: Word to check.
    :type word: str
    :param stopwords: Words to exclude.
    :type stopwords: iterable of str
    :rtype: bool
    """

    # Non-letter characters.
    try:
        word = strip_word(word)[1]
    except ValueError:
        return False

    # Too short.
    if len(word) < 3:
        return False

    word = word.lower()

    # Too few vowels.
    if all((v not in word) for v in VOWELS):
        return False

    # Stopword.
    if word in stopwords:
        return False

    return True


def is_spoonerizable_word_pair(word1, word2):
    """Check whether a word pair is spoonerizable.

    A spoonerizable word pair consists of two words \
    that do not share either a *head* or a *body* \
    (see :func:`split_word`).

    :param word1: First word.
    :type word1: str
    :param word2: Second word.
    :type word2: str
    :rtype: bool
    """

    # Deal with non-letter characters.
    try:
        word1 = strip_word(word1)[1]
        word2 = strip_word(word2)[1]
    except ValueError:
        return False

    head1, body1 = split_word(word1.lower())
    head2, body2 = split_word(word2.lower())

    return (head1 != head2) and (body1 != body2)


def is_valid_word(word, dictionary=None):
    """Check whether a word is valid.

    A valid word:

    * contains only letter characters ...
    * and is in ``dictionary``.

    If ``dictionary`` is ``None``, \
    any word is valid.

    :param word: Word to check.
    :type word: str
    :param dictionary: Known words.
    :type dictionary: iterable of str
    :rtype: bool
    """

    # Non-letter characters.
    try:
        word = strip_word(word)[1]
    except ValueError:
        return False

    if dictionary is None:
        return True

    return word.lower() in dictionary


def split_word(word):
    """Split a word into head and body.

    The *head* of a word is the first consonant cluster \
    up to but not including the first vowel. \
    The *body* is the remainder of the word. \
    Words that begin with a vowel have an empty head. \
    (See :data:`.regexes.CV_BOUNDARY`).

    ``'y'`` is treated as a vowel, \
    except at the beginning of a word. \
    If the letter combination ``'qu'``, \
    is followed by a vowel, \
    the ``'qu'`` is treated as a consonant.

    :param word: Word to split.
    :type word: str
    :return: head and body
    :rtype: tuple (str, str)
    """

    left, word, right = strip_word(word)

    head, body = CV_BOUNDARY.split(word, maxsplit=1)

    # Exception: Initial 'y' as consonant.
    if (not head[-1:].isalpha()) and body.lower().startswith('y'):
        head = head + body[0]
        body = body[1:]

    # Exception: 'qu'.
    elif head.lower().endswith('q') and body.lower().startswith('u'):
        if body[1:2] and (body[1:2].lower() in VOWELS):
            head = head + body[0]
            body = body[1:]

    return left + head, body + right


def copy_case_pattern(word, model):
    """Apply the *case pattern* of one word to another.

    Three case patterns are recognized:

    * *lowercase*: The first letter is lowercase.
    * *uppercase*: All letters are uppercase.
    * *capital*: The first letter is uppercase, \
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
