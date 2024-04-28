#!/bin/bash
#  sends POST request, and displays the body of the response
curl -s -H "email: test@gmail.com&subject: I will always be here for PLD" -X POST "$1"
