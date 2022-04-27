#Uses Python3
"""
Created on Mon Oct  5 10:33:36 2020

@author: cante
"""


m = int(input())

def moneychange(m): 
    coins = [10, 5, 1]
    ncoins = []
    for x in range(0,3):
        while m >= coins[x]:
            m -= coins[x]
            ncoins.append(coins[x])
    return(len(ncoins))

print(moneychange(m))