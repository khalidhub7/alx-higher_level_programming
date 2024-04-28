#!/bin/bash
# display the body of the response only if status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -sL "$1"
