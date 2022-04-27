#Uses python 3
"""
Created on Tue Sep 29 19:17:27 2020

@author: cante
"""
nn = [int(x) for x in input().split()]
n = nn[0]
m = nn[1]
def pisanoPeriod(m): 
    previous, current = 0, 1
    for i in range(0, m * m): 
        previous, current  = current, (previous + current) % m 
        
        
        if (previous == 0 and current == 1): 
            return i + 1
z = pisanoPeriod(m)
x = n%z

def fibonaiv(x,m):
    if x <= 1:
        return(x)
    else:
        f = list(range(x+1))
        f[0] = 0
        f[1] = 1
        
        for i in range(2,x+1):
            f[i] = (f[i-1] + f[i-2])%m
        return(f[i])
print(fibonaiv(x,m))