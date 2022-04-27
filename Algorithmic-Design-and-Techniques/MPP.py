#Uses python3
"""
Created on Tue Sep 22 12:17:49 2020

@author: cante
"""
n = input()
nn = [int(x) for x in input().split()]
def maxpairwise1(nn):
    max1 = max(nn)
    def compa(x):
        return(x == max1)
    compa1 = [compa(x) for x in nn]
    scompa1 = sum(compa1)
    if scompa1 != 1:
        return(max1 ** 2)
    else:
        def maxx2(x):
            if x != max1:
                return(x)
            else:
                return(0)
        nn2 = [maxx2(x)  for x in nn]
        max2 = max(nn2)
        return(max2 * max1)
print(maxpairwise1(nn))