#Python3 

from collections import deque


def BWH(string):
    processate = deque(string)
    BWHmatrix = []
    for x in range(0, len(processate)):
        processate.rotate()
        BWHmatrix.append("".join(list(processate)))
    return("".join([x[len(x)-1] for x in sorted(BWHmatrix)]))


def main():
    string = str(input())
    r = BWH(string)
    print(r)

if __name__ == "__main__":
    main()