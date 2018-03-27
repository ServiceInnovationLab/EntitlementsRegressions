# EntitlementsRegressions

[![Build Status](https://travis-ci.org/ServiceInnovationLab/EntitlementsRegressions.svg?branch=master)](https://travis-ci.org/ServiceInnovationLab/EntitlementsRegressions)
[![Waffle.io - Columns and their card count](https://badge.waffle.io/ServiceInnovationLab/EntitlementsRegressions.svg?columns=all)](https://waffle.io/ServiceInnovationLab/EntitlementsRegressions)


Runs regression tests against Regulation as a Platform - tests a set of persona are entitled to the correct benefits.

## How to configure and run
(for more clues see .travis.yml)

### Configure 
1. Obtain an API token for RaaP (nz)
1. Set as TOKEN in your env (see `env-sample`) 
1. Create python virtual env to run in and install dependencies (see more instructions below) 

### run tests
```
nosetests 
```

## Setting up environment

Make a new python virtual env to work in (you only need to do this once per project)
```
mkvirtualenv EntitlementsRegressions
```

When you want to run this tests, do this first:
```
workon EntitlementsRegressions
```

To install the dependencies in your virtual env:
```
pip install -r requirements.txt
```

make a `.env` file. See `env-example`


## Running the python tests

```
nosetests pytests
```
## For Mac users

If you're having issues installing the Virtual Environment wrapper, try a clean install as follows:

```
$ pip uninstall virtualenvwrapper
$ pip uninstall virtualenv

# if you have python installed in brew
$ brew uninstall python
$ brew remove python

$ brew install python
$ pip install virtualenv
$ pip install virtualenvwrapper
# or
$ sudo easy_install virtualenvwrapper

```

If you're still experiencing errors, you may need to modify your PATH in `~/.bash_profile`:

`vim ~/.bash_profile`
add or modify the following:
```
PATH="/Library/Frameworks/Python.framework/Versions/3.5/bin:${PATH}"
export PATH
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python
export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv
export VIRTUALENVWRAPPER_VIRTUALENV_ARGS='--no-site-packages'
source /usr/local/bin/virtualenvwrapper.sh
```

## Linters
This repo uses linter configuration from overcommit. to run:
1. `gem install overcommit`
1. `overcommit --install`
1. `overcommit --run`


## See also

Postman generated API docs for NZ Entitlements
https://documenter.getpostman.com/view/3560032/collection/7TJDZ5a
