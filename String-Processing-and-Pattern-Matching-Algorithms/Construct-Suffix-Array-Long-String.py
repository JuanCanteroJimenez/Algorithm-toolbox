#Python3
import itertools









def sortCharacters(S):
    
    simbols = {"$":0, "A":1, "C":2, "T":4, "G":3}
    order = list(itertools.repeat(0,len(S)))
    count = list(itertools.repeat(0,len(simbols)))

    for i in range(0, len(S)):
        count[simbols[S[i]]] = count[simbols[S[i]]] + 1
    for j in range(1, len(simbols)):
        count[j] = count[j] + count[j-1]
    for i in  range(len(S)-1, -1, -1):
        c = simbols[S[i]]
        count[c] = count[c] - 1
        order[count[c]] = i
    return(order)

def computeCharclasess(S, order):
    clase = list(itertools.repeat(0,len(S)))
    clase[order[0]] = 0
    for i in range(1, len(S)):
        if S[order[i]] != S[order[i-1]]:
            clase[order[i]] = clase[order[i-1]] + 1
        else:
            clase[order[i]] = clase[order[i-1]]
    return(clase)

def Sortdoubled(S, L, order, clase):
    count = list(itertools.repeat(0,len(S)))
    neworder = list(itertools.repeat(0,len(S)))
    for i in range(0,len(S)):
        count[clase[i]] = count[clase[i]] + 1
    for j in range(1, len(S)):
        count[j] = count[j] + count[j-1]
    for i in range(len(S)-1, -1, -1):
        start = (order[i]-L+len(S)) % len(S)
        cl = clase[start]
        count[cl] = count[cl] - 1
        neworder[count[cl]] = start
    return(neworder)

def UpdateClasses(newOrder, clase, L):
    n = len(newOrder)
    newclase = list(itertools.repeat(0,n))
    newclase[newOrder[0]] = 0
    for i in range(1, n):
        cur = newOrder[i] 
        prev = newOrder[i-1]
        mid = cur + L 
        midprev = (prev + L) % n
        if clase[cur] != clase[prev] or clase[mid] != clase[midprev]:
            newclase[cur] = newclase[prev] + 1
        else:
            newclase[cur] = newclase[prev]
    return(newclase)
def buildsuffixarray(S):
    order = sortCharacters(S)
    clase = computeCharclasess(S, order)
    L = 1
    while L < len(S):
        order = Sortdoubled(S, L, order, clase)
        clase = UpdateClasses(order, clase, L)
        L = L * 2
    return(order)

 











def main():
    j = str(input()) 
    order = buildsuffixarray(j)
    print(*order)
    




if __name__ == "__main__":
    main()