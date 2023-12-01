#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if (len(sys.argv)-1) == 0:
        print("0 arguments.")
    elif (len(sys.argv)-1) == 1:
        print("1 argument:\n1: {}".format(sys.argv[1]), end="\n")
    else:
        print("{} arguments:".format((len(sys.argv)-1)), end="\n")
        for i in range (len(sys.argv)-1):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
