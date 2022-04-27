#Uses python3
"""
Created on Sun Oct 11 22:03:50 2020

@author: cante
"""

n = int(input())
nn = [int(x) for x in input().split()]

def majoriti(nn):
    nn.sort()
    n = 1
    for i in range(1,len(nn)):
        
        if nn[i-1] == nn[i]:
            n += 1
            
        else:
            n = 1
        
        if n > len(nn)/2:
            return(1)
    return(0)
        
print(majoriti(nn))