#Uses Python3
"""
Created on Tue Oct  6 21:46:22 2020

@author: cante
"""

def largest(digits):
    answer = []
    def greatequal(x,maxdigit): 
        t = int(str(x)+str(maxdigit))
        f = int(str(maxdigit) + str(x))
        if t >= f:
            return(True)
        else:
            return(False)

        
    n = 1
    while n != 0:
        maxdigit = 0 
       
        for x in digits:
            if greatequal(x,maxdigit):
                maxdigit = x
        answer.append(maxdigit)
        digits.remove(maxdigit)
        
        n = len(digits)
        
    return(answer)

n = int(input())
digits = [int(x) for x in input().split()]
print("".join(map(str,largest(digits))))
            
