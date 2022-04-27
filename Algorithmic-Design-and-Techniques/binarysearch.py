#Uses python3


A = [int(x) for x in input().split()]
del A[0]

B = [int(x) for x in input().split()]

del B[0]

def binary(A,key):
    low = 0
    high = len(A)-1
    
    while low <= high:
        mid = low + (high-low)//2
        
        if key == A[mid]:
            return (mid)
        if key < A[mid]:
            high = mid -1
        else:
            low = mid + 1
        
    return(-1)
result = []

for key in B:
    n = binary(A,key)
    result.append(n)
    
print(" ".join(map(str,result)))