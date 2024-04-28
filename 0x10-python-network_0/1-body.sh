#!/bin/bash
# send GET request to URL and display body of response
a=$(curl -X GET "$1")
if("$a" == '200 OK');
	then
		echo"$a"
fi
