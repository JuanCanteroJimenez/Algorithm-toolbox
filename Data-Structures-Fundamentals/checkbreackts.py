#Python3
from collections import deque
import re

def Isbalanced(strin):
    st = str(strin)
    
    stack = deque()
    orden = 0
    acabado = []
    for char in st:
        orden = orden + 1
        if (char in "[{(") or (char in ")}]"): 
            
            if char in "[{(":
                acabado.append(orden)
                stack.append(char)
            else:
                if len(stack) == 0:
                    
                    return(orden)

                top = stack.pop()
                if (top == "[" and char != "]") or (top == "(" and char != ")") or (top == "{" and char != "}"):
                    
                    return(orden)
                else:
                    acabado.pop()
        
    if len(stack) == 0:
        return("Success")
    
    else:
        
        return(acabado[0])
    

print(Isbalanced(input()))