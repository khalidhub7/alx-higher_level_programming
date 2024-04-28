#!/bin/bash
#  send JSON POST request, and display body of response
curl -s -X POST -d @my_json_0 "$1"
