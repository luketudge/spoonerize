# -*- coding: utf-8 -*-

import setuptools


setuptools.setup(
    name='spoonerize',
    version='0.1',
    description='Search a text for potential spoonerisms.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/luketudge/spoonerize',
    author='Luke Tudge',
    author_email='luketudge@gmail.com',
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'],
    packages=['spoonerize'],
    install_requires=['regex'],
    python_requires='>=3',
    package_data={'spoonerize': ['data/*']}
)
