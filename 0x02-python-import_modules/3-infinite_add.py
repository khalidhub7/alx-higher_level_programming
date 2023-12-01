if __name__ == "__main__":
    import sys
    sum = 0
    if len(sys.argv) - 1 == 0:
        print("0")
    elif len(sys.argv) - 1 > 0:
        for i in range (len(sys.argv) - 1):
            sum += int(sys.argv[i + 1])
        print(sum)
