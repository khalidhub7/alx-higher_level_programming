#!/bin/bash
#  send JSON POST request, and display body of response
curl -s -X POST -d @"$2" -H "Content-Type: application/json" "$1"
