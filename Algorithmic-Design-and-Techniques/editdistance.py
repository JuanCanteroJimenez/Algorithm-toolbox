#Uses python3
"""
Created on Mon Oct 19 17:38:07 2020

@author: cante
"""
import numpy as np
A = input()
B = input()

def editdistance(A, B):
    A, B = " " + A, " " + B
    tamaño = len(A), len(B)
   
    D = np.zeros(tamaño)
    
    D[0,] = range(0,tamaño[1])
    D[:,0] = range(0,tamaño[0])
    for j in range(1,tamaño[1]):
        for i in range(1,tamaño[0]):
            insetion = D[i,j-1] + 1
            deletion = D[i-1,j] + 1
            match = D[i-1,j-1]
            mismatch = D[i-1,j-1] + 1
            if A[i] == B[j]:
               
                
                D[i,j] = min(insetion, deletion, match)
            else:
                
                
                D[i,j] = min(insetion, deletion, mismatch)
            
   
    return(int(D[tamaño[0]-1,tamaño[1]-1]))
print(editdistance(A, B))