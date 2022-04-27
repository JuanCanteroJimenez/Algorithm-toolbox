#Uses python3
"""
Created on Tue Sep 22 13:09:13 2020

@author: cante
"""
x = int(input())
def fibonaiv(x):
    if x <= 1:
        return(x)
    else:
        f = list(range(x+1))
        f[0] = 0
        f[1] = 1
        
        for i in range(2,x+1):
            f[i] = (f[i-1] + f[i-2])%10
        return(f[x])
print(fibonaiv(x))