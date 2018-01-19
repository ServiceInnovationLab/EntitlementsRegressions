#!/bin/bash

set -euv

test_dir='./tests'

for collection in "$test_dir"/*
do
  echo "$collection"
  node_modules/.bin/newman run $collection -e ./postman_env.json
done

