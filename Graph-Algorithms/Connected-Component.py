#Python3
import sys
import threading

class vertex:
    def __init__(self):
        self.postvisit = None
        self.previsit = None
        self.visited = 0
class graph:
    def __init__(self,vertexs):
        self.ladjacent = [[] for x in range(0,vertexs)]
        self.vertices = {x:vertex() for x in range(1,vertexs+1)}
    def addedge(self,v1,v2):
        if v2  not in self.ladjacent[v1-1]:
            self.ladjacent[v1-1].append(v2)
        if v1  not in self.ladjacent[v2-1]:
            self.ladjacent[v2-1].append(v1)
    def explore(self,vertice):
        self.vertices[vertice].visited = 1
        for x in range(0,len(self.ladjacent[vertice-1])):
            if self.vertices[self.ladjacent[vertice-1][x]].visited == False:
                self.explore(self.ladjacent[vertice-1][x])
    def areachablefromb(self,a,b):
        self.explore(a)
        return(self.vertices[b].visited)
    def explore2(self):
        n = 0
        for x in range(1,len(self.ladjacent)+1):
            if self.vertices[x].visited == 0:
                self.explore(x)
                n += 1
        return(n)

def main():
    features = [int(x) for x in input().split()]
    grafo = graph(features[0])
    for x in range(0,features[1]):
        n = [int(i) for i in input().split()]
        grafo.addedge(n[0],n[1])
    print(grafo.explore2())
        
    



if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()