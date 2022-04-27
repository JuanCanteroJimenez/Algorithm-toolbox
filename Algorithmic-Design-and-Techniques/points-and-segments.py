#Uses python3
"""
Created on Thu Oct 15 12:25:42 2020

@author: cante
"""
n = [int(x) for x in input().split()]


segments = []
for x in range(0,n[0]):
    m = [int(x) for x in input().split()]
    segments.append(m)
    
points = [int(x) for x in input().split()]
segments.sort()
result = []
def loteryfast(segments, points,result):
    
    if len(points) == 1:
        n = 0
        for x in segments:
            if points[0] >= x[0]:
                if points[0] <= x[1]:
                   n += 1
            else:
                break
        result.append(n)
        
        return(result)
    else: 
        m = len(points)//2
        loteryfast(segments, points[:m],result)
        loteryfast(segments, points[m:],result)
    return(result)
n = loteryfast(segments,points,result)
print(" ".join(map(str,n)))