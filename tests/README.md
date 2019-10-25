# Tests

This directory contains the tests for the *spoonerize* package.

The shell script [test_install.sh](test_install.sh) builds the package from source locally, runs all the tests, and additionally builds a local copy of the documentation to check that that works too.

The Python tests are written for [pytest](https://docs.pytest.org). Those in [test_module.py](test_module.py) test only the main functions intended for the 'end spooner'. The others test each submodule in more detail.

The Python script [test_file.py](test_file.py) searches for and applies all valid spoonerisms in the full text of Moby Dick. Currently, this test is very slow, so is not included in the default testing suite. (The text of Moby Dick is taken from [Project Gutenberg](https://www.gutenberg.org/).)
