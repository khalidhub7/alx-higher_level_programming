#!/bin/bash
# send GET request to URL and display body of response
curl -sL "$1" # -L: use for follow redirections
