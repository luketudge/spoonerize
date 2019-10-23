#!/bin/bash

# Use requirements.txt just for the testing environment.
# Make this reproducible by pinning all versions.
pip install -r requirements.txt

# Use setup.py for actual package dependencies.
# Don't pin these.
python setup.py bdist_wheel
pip install --force-reinstall dist/spoonerize*.whl
