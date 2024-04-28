#!/bin/bash
# displays all HTTP methods that server will accept
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
