# spoonerize

A Python package for working with [spoonerisms](https://en.wikipedia.org/wiki/Spoonerism). For party fun.

* [Aims](#aims)
* [Alternatives](#alternatives)
* [Install](#install)
* [Contribute](contributing.md)

## Aims

* Spoonerize pairs of words:
  - Handle special letter sequences such as *y* and *qu* correctly in context.
  - Preserve the case pattern of a word after spoonerization.
* Spoonerize whole texts by searching for spoonerizable pairs of words.

## Alternatives

The [spooner](https://github.com/danmaps/spooner) package by Vanny McDey already does a good job of incorporating phonetics into single word-pair spoonerisms. Which is pretty cool. The *spoonerize* package won't reinvent this, and will stick to purely 'letter-transposition' spoonerisms (at least for the moment).

## Install

To install you will need Python 3.

### Virtual environment

Have a virtual environment ready into which to install the package. It's best not to install third-party packages into your root environment. And I'm probably the thirdest party there is.

For example, create and activate a virtual environment using *virtualenv* as described in the [Hitchhiker's Guide to Python](https://docs.python-guide.org/dev/virtualenvs/#lower-level-virtualenv):

```shell
virtualenv -p /usr/bin/python3 .venv
source .venv/bin/activate
```

You may need to replace `/usr/bin/python3` with the path to your Python 3 executable. And you may want to replace `venv` with a prettier name for your virtual environment.

### Clone repository

Clone this repository to download the latest source code, then switch into the newly-cloned directory:

```shell
git clone https://github.com/luketudge/spoonerize.git
cd spoonerize
```

### Install and test

Run the installation and testing script [test_install.sh](tests/test_install.sh) to install the package and then run the tests (you may need to change the permissions for this file to allow executing it as a program):

```python
./tests/test_install.sh
```

If you make changes to the source code (in the main package directory [spoonerize](spoonerize)), you can run this script again to build and test your modified version.
