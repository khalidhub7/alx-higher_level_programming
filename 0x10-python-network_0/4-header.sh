#!/bin/bash
# sends GET request to diplay value of some variable
curl -sI -H "X-School-User-Id: 98" -X GET "$1"
