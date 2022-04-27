#Uses python3
"""
Created on Mon Oct 19 17:38:07 2020

@author: cante
"""
import numpy as np
A = input()
AA = [int(x) for x in input().split()]
B = input()
BB = [int(x) for x in input().split()]
def editdistance(A, B):
    A, B = [0] + A, [0] + B
    tamaño = len(A), len(B)
   
    D = np.zeros(tamaño)
    
    
    for j in range(1,tamaño[1]):
        for i in range(1,tamaño[0]):
            insetion = D[i,j-1]
            deletion = D[i-1,j] 
            match = D[i-1,j-1] + 1
            mismatch = D[i-1,j-1] 
            if A[i] == B[j]:
               
                
                D[i,j] = max(insetion, deletion, match)
            else:
                
                
                D[i,j] = max(insetion, deletion, mismatch)
            
    
    return(int(D[tamaño[0]-1,tamaño[1]-1]))
print(editdistance(AA, BB))