#Uses Python3
"""
Created on Tue Oct 27 09:55:10 2020

@author: cante
"""

nn = [int(x) for x in input().split()]
W = nn[0]
lig = [int(x) for x in input().split()]
import numpy as np

def gold(W, lig):
    tamaño = (len(lig)+1,W+1)
    lig = [0] + lig
    value = np.zeros(tamaño)
    for i in range(1,len(lig)):
        for w in range(1,W+1):
            value[i,w] = value[i-1,w]
            if lig[i] <= w:
                val = value[i-1,w-lig[i]] + lig[i]
                if value[i,w] < val:
                    value[i,w] = val
    
    return(value[len(lig)-1,W])
print(int(gold(W,lig)))