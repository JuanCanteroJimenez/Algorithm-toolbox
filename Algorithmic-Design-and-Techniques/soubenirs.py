#Uses Python3
"""
Created on Tue Oct 27 10:35:59 2020

@author: cante
"""
import numpy as np
def sou(lig):
    if sum(lig)%3 != 0:
        return(0)
    if len(lig) == 3 and lig[0]==lig[1]==lig[2]:
        return(1)
    if len(lig) <= 3:
        return(0)
    else:
        n = [0,0,0]
        W = sum(lig)
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
                        if val == (W/3):
                            n[0] = 1
                        if val == (W/3)*2:
                            n[1] = 1
                        if val == W:
                            n[2] = 1
        
        if sum(n) == 3:
            return(1)
        else: 
            return(0)
n = input()
lig = [int(x) for x in input().split()]
print(sou(lig))                 
        