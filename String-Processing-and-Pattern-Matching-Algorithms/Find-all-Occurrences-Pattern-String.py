#Python3
import itertools


def polyhash(S, p, x):
    hash = 0 
    for i in range(len(S)-1, -1, -1):
        hash = (hash * x + ord(S[i])) % p
    return(hash)

def polyhash1(S, p, x):
    hash = 0 
    for i in range(0,len(S)):
        hash = (hash + x**i * ord(S[i])) % p
    return(hash)

def precomputehashes(T, P, p, x):
    H = list(itertools.repeat(0, len(T)-len(P) + 1))
    S = T[len(T)-len(P):len(T)]
    H[len(T)- len(P)] = polyhash(S, p, x)
    y = 1
    for i in range(0, len(P)):
        y = (y*x) % p
    for i in range(len(T)-len(P) - 1, -1,-1):
        H[i] = (x*H[i+1] + ord(T[i]) - y*ord(T[i + len(P)])) % p
    return(H)



def RabinKarp(T, P):
    if len(P) > len(T):
        return( [])
    p, x = 1000000009, 31
    positions = []
    pHash = polyhash(P, p, x)
    H = precomputehashes(T, P, p, x)
    for i in range(0, len(T)- len(P)+1):
        if pHash == H[i]:
            if T[i: i + len(P)] == P: 
                positions.append(i)
    return(positions)



def computeprefix(P):
    s = list(itertools.repeat(0,len(P)))
    s[0], border = 0,0
    for i in range(1, len(P)):
        while border > 0 and P[i] != P[border]:
            border = s[border-1]
        if P[i] == P[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border
    return(s)

def findallocurrences(P, T):
    S = P + "$" + T
    s = computeprefix(S)
    result = []
    for i in range(len(P)+1, len(S)):
        if s[i] == len(P):
            result.append(i-2*len(P))
    return(result)



def main():
    P = str(input())
    T = str(input())
    print(*findallocurrences(P, T))

if __name__ == "__main__":
    main()

