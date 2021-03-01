#!/bin/bash

# Check that we are in a virtual environment.
# (Prevents accidentally installing into the root environment).
if test -z "$VIRTUAL_ENV"
then
    echo "No virtual environment detected. Exiting."
    exit 1
fi

# Use requirements.txt just for the testing environment.
pip install -r requirements.txt

# Use setup.py for actual package dependencies.
python setup.py bdist_wheel
pip install --force-reinstall dist/spoonerize*.whl
