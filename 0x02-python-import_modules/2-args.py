#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    gg = len(sys.argv)-1
    if gg == 0:
        print("0 arguments.")
    elif gg == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]), end="\n")
    else:
        print("{} arguments:".format(gg), end="\n")
        for i in range (gg):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
