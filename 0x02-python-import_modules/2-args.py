#!/usr/bin/python3
import sys
if (len(sys.argv)-1) == 0:
    print("0 arguments.")
elif (len(sys.argv)-1) == 1:
    print("1 argument:", end="\n")
    print("1: {}".format(sys.argv[1]))
else:
    print("{:d} arguments:".format((len(sys.argv)-1)), end="\n")
    for i in range (len(sys.argv)-1):
        print("{:d}: {:s}".format(i + 1, sys.argv[i + 1]))
