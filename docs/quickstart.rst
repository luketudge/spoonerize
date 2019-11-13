Quickstart
==========

.. highlight:: python3

Import the module::

    import spoonerize as sp

Spoonerize a word pair::

    sp.spoonerize_word_pair('crushing', 'blow')

Spoonerize all suitable word pairs in a phrase::

    sp.spoonerize_text('A crushing blow.')

Exclude custom `stop words <https://en.wikipedia.org/wiki/Stop_words>`_::

    sp.spoonerize_text('She dealt him a crushing blow.', stopwords=['she', 'him'])

Exclude words not in a custom dictionary::

    sp.spoonerize_text('She dealt him a crushing blow.', dictionary=['blushing', 'crow'])

Or use the pre-compiled wordlists::

    from spoonerize.wordlists import STOPWORDS, DICTIONARY
    sp.spoonerize_text('She dealt him a crushing blow.', stopwords=STOPWORDS, dictionary=DICTIONARY)
