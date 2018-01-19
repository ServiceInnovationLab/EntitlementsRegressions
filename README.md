# EntitlementsRegressions

[![Build Status](https://travis-ci.org/ServiceInnovationLab/EntitlementsRegressions.svg?branch=master)](https://travis-ci.org/ServiceInnovationLab/EntitlementsRegressions)

Runs regression tests against Regulation as a Platform - tests a set of persona are entitled to the correct benefits.

## How to configure and run
(for more clues see .travis.yml)

1. Obtain an API token for RaaP (nz)
1. Set as TOKEN in your env
1. `npm install` to get dependencies
1. run `./bin/make_postman_env.sh` to create a config file for Postman
1. node_modules/.bin/newman run tests/*.json -e ./postman_env.json


## Linters
This repo uses linter configuration from overcommit. to run:
1. `gem install overcommit`
1. `overcommit --install`
1. `overcommit --run`

