#!/bin/bash
#  make request to given url
curl -s -X PUT -d "user_id=98" -d "You got me!" "http://0.0.0.0:5000/catch_me"
