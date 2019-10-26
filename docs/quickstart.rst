Quickstart
==========

.. highlight:: python3

Import the module::

    import spoonerize as sp

Spoonerize a word pair::

    sp.spoonerize_word_pair('party', 'fun')

Spoonerize all suitable word pairs in a phrase, excluding custom stopwords::

    sp.spoonerize_text('Party fun with sleeping bags.', stopwords=('with',))

Or use the wordlists provided::

    stopwords = sp.wordlists.STOPWORDS
    sp.spoonerize_text('Party fun with sleeping bags.', stopwords=stopwords)
