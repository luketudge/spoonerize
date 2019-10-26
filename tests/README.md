# Tests

This directory contains the tests for the *spoonerize* package.

The shell script [test_install.sh](test_install.sh) builds the package from source locally, runs all the tests, and additionally builds a local copy of the documentation to check that that works too.

The Python tests are written for [pytest](https://docs.pytest.org). Those in [test_module.py](test_module.py) test only the main functions intended for the 'end spooner'. The others test each submodule in more detail.

The two tests in [test_performance.py](test_performance.py) search for spoonerisms in the full text of Moby Dick (the text is taken from [Project Gutenberg](https://www.gutenberg.org/)). These tests each take nearly 5 seconds to run on my fairly standard Ubuntu laptop. For repeated testing, you can run the test suite without the speed tests using pytest's `-k` option:

```shell
pytest -k 'not speed'
```
