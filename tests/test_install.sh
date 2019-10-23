#!/bin/bash -v

# Run this from the project root directory,
# where install.sh is located.

# Install.
./install.sh

# Run the tests.
pytest -ra -v

# Build the documentation.
make -C docs html
