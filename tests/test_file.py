#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Search for spoonerisms in a large text file.
"""

import os
import timeit

from spoonerize import spoonerize_text
from spoonerize.wordlists import DICTIONARY
from spoonerize.wordlists import STOPWORDS


#%% Setup.

# Load test text.
filename = 'melville-moby_dick.txt'
filepath = os.path.join(os.path.dirname(__file__), filename)
filesize = os.path.getsize(filepath)
text = open(filepath, encoding='utf-8').read()

# Format for printed output.
output_format = '''
#### {}
{}
->
{}
'''

# Function to run in timeit().
def spoonerize_test_file():

    counter = 0

    for sentence in text.split('.'):
        sentence_spoon = spoonerize_text(sentence,
                                         stopwords=STOPWORDS,
                                         dictionary=DICTIONARY)
        if sentence_spoon != sentence:
            counter = counter + 1
            print(output_format.format(counter, sentence, sentence_spoon))


#%% Run.

if __name__ == '__main__':

    t = timeit.timeit('spoonerize_test_file()', number=1, globals=globals())
    msg = "'{}'' ({} bytes) spoonerized in {} s."
    print(msg.format(filename, filesize, t))
