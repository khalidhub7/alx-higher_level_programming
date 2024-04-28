#!/bin/bash
# sends GET request to diplay value of some variable
curl -sI "$1" | grep "X-School-User-Id" | cut -d ':' -f2 | tr -d '[:space:]'
