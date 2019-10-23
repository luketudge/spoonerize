#!/bin/bash -v

# Run this from the project root directory,
# where install.sh is located.

# Check that we are in a virtual environment.
# (Prevents accidentally installing into root environment).
if test -z "$VIRTUAL_ENV"
then
    echo "No virtual environment detected. Exiting."
    exit 1
fi

# Install.
./install.sh

# Run the tests.
pytest -v

# Build the documentation.
make -C docs html
