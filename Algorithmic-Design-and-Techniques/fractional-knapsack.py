#Uses Python 3
"""
Created on Mon Oct  5 14:34:05 2020

@author: cante
"""

nmaxW = [int(x) for x in input().split()]
valores = []
W = nmaxW[1]
for x in range(nmaxW[0]):
    x = [int(x) for x in input().split()]
    valores.append(x)

def maxloot(valores,W, n): 
    for i in range(len(valores)):
        valores[i] = [valores[i][0]/valores[i][1],valores[i][1]]
    valoresso = sorted(valores, reverse=True)
    j = 0
    total = 0
    
    while W > 0 and j < n :
        c = min(W, valoresso[j][1])
        W -= c
        total += c*valoresso[j][0]
        j += 1
    return(round(total,4))
print(maxloot(valores,W,nmaxW[0]))

