#Uses python3
"""
Created on Wed Sep 30 12:03:03 2020

@author: cante
"""

nn = [int(x) for x in input().split()]
m = nn[0]

pp10 = 60
sPP10 = 280
x = m%pp10

def fibonaiv(x):
    if x <= 1:
        return(x)
    else:
        f = list(range(x+1))
        f[0] = 0
        f[1] = 1
        n = 1
        for i in range(2,x+1):
            f[i] = (f[i-1] + f[i-2])%10
            n += f[i]
        return(n%10)

print(z)
