#!/bin/bash
#  make request to given url
curl -s -X POST -d "You got me!" "http://0.0.0.0:5000/catch_me"
