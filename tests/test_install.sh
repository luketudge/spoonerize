#!/bin/bash -v

# Run this from the project root directory,
# where install.sh is located.

# Install.
./install.sh

# Run the tests and coverage report.
pytest -v --cov-report term-missing --cov=spoonerize tests/

# Build the documentation.
make -C docs html
