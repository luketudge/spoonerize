#!/bin/bash -v

# Run this from the project root directory,
# where install.sh is located.

# Install.
./install.sh

# Run the tests and coverage report.
pytest -v --cov=spoonerize --cov-report=term-missing 

# Build the documentation.
make -C docs html
