#!/usr/bin/python3
import sys
if (len(sys.argv)-1) == 0:
    print("0 arguments.")
else:
    print("{} arguments:".format((len(sys.argv)-1)), end="\n")
    for i in range (len(sys.argv)-1):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
