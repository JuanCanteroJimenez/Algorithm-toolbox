#Uses Python3
"""
Created on Tue Oct  6 16:57:08 2020

@author: cante
"""

n = int(input())

def maxreward(n):
    
    i = 0
    j = 1
    ks = []
    nn = n
    while i != nn:
        
        n = n - j
        
        
        
        if n <= j:
            j = j + n
            ks.append(j)
        else:
            ks.append(j)
        i += j
        j += 1
        
    return(ks, len(ks))
z = maxreward(n)
print(z[1])
print(" ".join(map(str,z[0])))
