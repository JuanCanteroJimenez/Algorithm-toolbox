#Uses python3
"""
Created on Tue Sep 22 19:16:07 2020

@author: cante
"""

def gcd3(x,xx):
    a = min([x,xx])
    b = max([x,xx])
    i = 1
    while i == 1:
        x = b%a
        if x == 0:
            return(a)
            break
        else:
            b = a
            a = x

n = [int(x)for x in input().split()]
print((n[1]*n[0])//(gcd3(n[1],n[0])))