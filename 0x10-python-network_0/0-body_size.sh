#!/bin/bash
# display the length of conetent
curl -sI $@ | grep 'Content-Length:' | cut -d ' ' -f2
