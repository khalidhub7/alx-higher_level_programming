#!/bin/bash
# send GET request to URL and display body of response
curl -s -w "%{http_code}" "$1" | awk 'END{if($0==200)print body}{body=body $0 ORS}'
