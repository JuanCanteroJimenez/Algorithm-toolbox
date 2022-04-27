#Python3 

from collections import deque
import re

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    
    return [ atoi(c) for c in re.split(r'(\d+)', text) ]


def BWH(string):
    processate = deque(string)
    BWHmatrix = []
    for x in range(0, len(processate)):
        processate.rotate()
        BWHmatrix.append("".join(list(processate)))
    return("".join([x[len(x)-1] for x in sorted(BWHmatrix)]))

def BHWinversenaive(BHWs):
    processate = [deque(x) for x in BHWs]
    processate.sort()
    for x in range(0,len(BHWs)-1):
        [processate[x].appendleft(BHWs[x])  for x in range(0,len(BHWs))]

        processate.sort()
    processate.sort()
    processate[0].rotate(-1)
    return("".join(list(processate[0])))

def BWHreverse(BWHs):
    BWHs = [BWHs[x]+str(x) if BWHs[x] != "$" else BWHs[x]  for x in range(0,len(BWHs))]
    BWH_sort = sorted(BWHs,key=natural_keys)
    dicti = {BWHs[x]:BWH_sort[x]  for x in range(0,len(BWHs))}
    BWHs_re = ""
    first = "$"
    while len(BWHs_re) < len(BWHs):
        BWHs_re = BWHs_re + dicti[first][0]
        first = dicti[first]
    return(BWHs_re)  



    





def main():
    string = str(input())
    
   
    h = BWHreverse(string)
    print(h)
    


if __name__ == "__main__":
    main()