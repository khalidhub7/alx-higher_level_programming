#!/bin/bash
# send GET request to URL and display body of response
a="$(curl -s -o /dev/null -w "%{http_code}" "$1")" && [ $a -eq 200 ] && curl -sL "$1"
