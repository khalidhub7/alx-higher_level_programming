#!/bin/bash
# send DELETE request to URL and displays the body of response
curl -X DELETE "$1" && curl -X GET "$1"
