#!/bin/bash
# sends request URL, and display the size of body
curl -X GET "$1" | wc -c
