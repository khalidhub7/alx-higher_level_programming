#!/bin/bash
# sends GET request to diplay value of some variable
curl -sI -X GET -H "X-School-User-Id: 98" "$1"
