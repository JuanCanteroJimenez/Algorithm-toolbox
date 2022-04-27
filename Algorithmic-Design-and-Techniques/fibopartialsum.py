#Uses python3
"""
Created on Wed Sep 30 12:03:03 2020

@author: cante
"""

nn = [int(x) for x in input().split()]
m = nn[0]
n = nn[1]
pp10 = 60
sPP10 = 280
if m == 0:
    x = (n-m)%pp10
else:
    x = (n-m)%pp10 +1


def fibonaivd(m):
    m = m%60
    if m <= 1:
        return([0,1])
    else:
        f = list(range(m+1))
        f[0] = 0
        f[1] = 1
        n = 1
        for i in range(2,m+1):
            f[i] = (f[i-1] + f[i-2])%10
            
        return([f[i-1]%10,f[i]%10])


def fibonaiv(x,z):
    if x == 0:
        return(z[0])
    else:
        f = list(range(x+1))
        f[0] = z[0]
        f[1] = z[1]
        n = z[1]
        for i in range(2,x+1):
            f[i] = (f[i-1] + f[i-2])%10
            n += f[i]
        return(n%10)

print(fibonaiv(x,fibonaivd(m)) + (((n-m)//60)*sPP10)%10)
