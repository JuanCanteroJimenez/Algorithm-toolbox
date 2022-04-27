#Uses Python3
"""
Created on Tue Oct  6 10:13:06 2020

@author: cante
"""
n = [int(x) for x in input().split()]
valores = []
for x in range(n[0]):
    x = [int(x) for x in input().split()]
    valores.append(x)
def segmented1 (valores, n):
    valores = sorted(valores, key = lambda x: x[1])
    points = []  
    i = 0
    def compa(y):
        if points[j] >= y[0] and points[j] <= y[1]:
            return(False)
        else:
            return(True)
    j = 0  
    while i == 0:
        points.append(valores[0][1])
        
        bol = map(compa, valores)
        valores = [x for (x,y) in zip(valores,bol) if y]
        j +=1
        if len(valores) == 0:
            i += 1
    return(points)


z = segmented1(valores,n[0])
print(len(z))
print(" ".join(map(str,z)))