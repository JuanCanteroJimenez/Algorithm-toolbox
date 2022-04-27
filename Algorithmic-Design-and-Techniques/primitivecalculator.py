#Uses python3
"""
Created on Thu Oct 15 19:14:06 2020

@author: cante
"""
m = int(input())

def primitive(m):
    moneycoins = [[0]] * (m + 1)
    moneycoins[0] = [-1]
    coins = [1, 2, 3]
    for x in range(1,m+1):
        
        moneycoins[x] = [float("inf")]
        for i in range(0,len(coins)):
            
            if 2 == coins[i] or 3 == coins[i]:
                if  x/coins[i] >= 1 and x%coins[i] == 0:
                    
                    ncoins = moneycoins[round(x/coins[i])][0] + 1
                    
                    if ncoins < moneycoins[x][0]:
                        
                        
                        moneycoins[x] = [ncoins] 
                        
                        moneycoins[x] = moneycoins[x] + moneycoins[round(x/coins[i])][1:] + [coins[i]]
                        
            else:
                if x-(x-coins[i]) >= 1:
                    ncoins = moneycoins[(x-coins[i])][0] + 1
                    
                    if ncoins < moneycoins[x][0]:
                        
                        moneycoins[x] = [ncoins] 
                        moneycoins[x] = moneycoins[x] + moneycoins[(x-coins[i])][1:] + [coins[i]]
    j = 1
    h = [1]
    for x in range(2,len(moneycoins[m])):
        if moneycoins[m][x] == 2 or moneycoins[m][x] == 3:
            j = j*moneycoins[m][x]
            h.append(j)
        else:
            j = j+moneycoins[m][x]
            h.append(j)
    
    return(moneycoins[m][0],h)    

n, i = primitive(m)
print(n)
print(" ".join(map(str,i)))