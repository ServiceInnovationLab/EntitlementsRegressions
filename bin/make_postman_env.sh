#!/bin/bash

FILENAME=./postman_env.json

cat > $FILENAME <<- EndOfConfig
{
  "id": "0d418806-6615-a7f1-a100-d6e008753d7f",
  "name": "RaaP API Env",
  "values": [
    {
      "enabled": true,
      "key": "token",
      "value": "$TOKEN",
      "type": "text"
    }
  ],
  "timestamp": 1516309420735,
  "_postman_variable_scope": "environment",
  "_postman_exported_at": "2018-01-18T22:43:03.675Z",
  "_postman_exported_using": "Postman/5.5.0"
}
EndOfConfig
