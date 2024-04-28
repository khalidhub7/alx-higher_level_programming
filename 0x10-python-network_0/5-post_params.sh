#!/bin/bash
#  sends POST request, and displays the body of the response
curl -s -d "email:test%40gmail.com&subject:I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
