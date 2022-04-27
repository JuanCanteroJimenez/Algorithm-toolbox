#Uses Python3
"""
Created on Mon Oct  5 10:33:36 2020

@author: cante
"""


m = int(input())

def moneychange(m): 
    coins = [4, 1, 3]
    ncoins = []
    for x in range(0,3):
        while m >= coins[x]:
            m -= coins[x]
            ncoins.append(coins[x])
    return(len(ncoins))

def dpmongeychange(m):
    moneycoins = [0] * (m + 1)
    coins = [1, 3, 4]
    for x in range(1,m+1):
        
        moneycoins[x] = float("inf")
        for i in range(0,len(coins)):
            if x >= coins[i]:
                ncoins = moneycoins[x-coins[i]] + 1
                
                
                if ncoins < moneycoins[x]:
                    moneycoins[x] = ncoins 
            
    return(moneycoins[m])
print(dpmongeychange(m))