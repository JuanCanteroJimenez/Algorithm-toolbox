#Python3

def dpmongeychange(m, coins):
    moneycoins = [0] * (m + 1)
    
    
    for x in range(1,m+1):
        
        moneycoins[x] = float("inf")
        for i in range(0,len(coins)):
            
            if x >= coins[i]:
                ncoins = moneycoins[x-coins[i]] + 1
                
                
                if ncoins < moneycoins[x]:
                    moneycoins[x] = ncoins 
            
    return(moneycoins[m])


def main():
    cuantity = int(input())
    denominations = [int(x) for x in input().split(",")]
    print(dpmongeychange(cuantity, denominations))

if __name__ == "__main__":
    main()