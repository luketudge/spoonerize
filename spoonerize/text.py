# -*- coding: utf-8 -*-
"""Functions for finding spoonerisms in multi-word texts.
"""

from .regexes import SENTENCE_BOUNDARY
from .regexes import WORD
from .word import is_spoonerizable_word
from .word import is_valid_word
from .word import spoonerize_word_pair


#%% Main function.

def spoonerize_text(text, maxdist=1, stopwords=(), dictionary=None):
    """Spoonerize all valid word pairs in a text.

    All valid word pairs in ``text`` are spoonerized \
    (see :func:`find_valid_word_pairs`).

    :param text: Text to spoonerize.
    :type text: str
    :param maxdist: Passed on to :func:`find_valid_word_pairs`.
    :type maxdist: int
    :param stopwords: Passed on to :func:`is_spoonerizable_word`.
    :type stopwords: iterable of str
    :param dictionary: Passed on to :func:`is_valid_word`.
    :type dictionary: iterable of str
    :return: Spoonerized text.
    :rtype: str
    """

    pos = 0
    text_new = []

    for match in find_valid_word_pairs(text, maxdist=maxdist, stopwords=stopwords, dictionary=dictionary):

        # Unpack the match into relevant components.
        match1, match2 = match
        start1, end1, word1 = match1
        start2, end2, word2 = match2

        # Add each slice to the new text.
        text_new.append(text[pos:start1])
        text_new.append(word1)
        text_new.append(text[end1:start2])
        text_new.append(word2)

        # Move on to the end of the second word.
        pos = end2

    # Add any remaining text.
    text_new.append(text[pos:])

    return ''.join(text_new)


#%% Helper functions.

def find_valid_word_pairs(text, maxdist=1, stopwords=(), dictionary=None):
    """Find valid word pairs in a text.

    A valid word pair:

    * consists of two *spoonerizable* words \
    (see :func:`.word.is_spoonerizable_word`) ...
    * within ``maxdist`` word positions of each other ...
    * that do not span a sentence boundary \
    (see :data:`.regexes.SENTENCE_BOUNDARY`) ...
    * or overlap with an existing valid pair, ...
    * and whose spoonerization results in two valid words \
    (see :func:`.word.is_valid_word`).

    Each of the two words in a valid word pair \
    is returned as a tuple of the form \
    (*start*, *end*, *new*), \
    where *start* and *end* are the indices of the word's position, \
    and *new* is the word's spoonerized form.

    :param text: Text to search.
    :type text: str
    :param maxdist: Maximum permitted distance \
    between words.
    :type maxdist: int
    :param stopwords: Passed on to :func:`is_spoonerizable_word`.
    :type stopwords: iterable of str
    :param dictionary: Passed on to :func:`is_valid_word`.
    :type dictionary: iterable of str
    :return: Successive word pairs.
    :rtype: iterator of tuples of \
    ((int, int, str), (int, int, str))
    """

    pos = 0
    text_end = len(text)

    while True:

        # Find the next word.
        word_match = WORD.search(text, pos)

        # If there is none, stop.
        if word_match is None:
            break

        # Get the position and text of the word.
        word_start, word_end = word_match.span()
        word = word_match[0]

        # Move on to the end of the word.
        pos = word_end

        if is_spoonerizable_word(word, stopwords=stopwords):

            # Find the next sentence boundary.
            boundary_match = SENTENCE_BOUNDARY.search(text, word_end)
            if boundary_match is None:
                sentence_end = text_end
            else:
                sentence_end = boundary_match.end()

            # Search for partner words up to the next sentence boundary.
            dist = 0
            for partner_match in WORD.finditer(text, word_end, sentence_end):

                # If the partner word is too far away, stop.
                dist = dist + 1
                if dist > maxdist:
                    break

                # Get the text of the partner word.
                partner = partner_match[0]

                if is_spoonerizable_word(partner, stopwords=stopwords):

                    # Spoonerize them.
                    word_spoon, partner_spoon = spoonerize_word_pair(word, partner)

                    if is_valid_word(word_spoon, dictionary=dictionary) and is_valid_word(partner_spoon, dictionary=dictionary):

                        # Get the position of the partner word.
                        partner_start, partner_end = partner_match.span()

                        # Return the pair.
                        word_result = (word_start, word_end, word_spoon)
                        partner_result = (partner_start, partner_end, partner_spoon)
                        yield (word_result, partner_result)

                        # Continue the search from the end of the partner word.
                        pos = partner_end
                        break
