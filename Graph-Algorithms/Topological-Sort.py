#Python3
import sys
import threading

class vertex:
    def __init__(self):
        self.postvisit = None
        self.previsit = None
        self.visited = False
class order:
    def __init__(self):
        
        self.clock = 0
    def previsit(self):
        self.clock += 1
        return(self.clock)
    def postvisit(self):
        self.clock += 1
        return(self.clock)

class graph:
    def __init__(self,vertexs):
        self.ladjacent = [[] for x in range(0,vertexs)]
        self.vertices = {x:vertex() for x in range(1,vertexs+1)}
        self.circular = 0
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
    def addedge_direct(self,v1,v2):
        if v2  not in self.ladjacent[v1-1]:
            self.ladjacent[v1-1].append(v2)
    def explore2(self,vertice,clock):
        n = 0
        self.vertices[vertice].visited = True
        self.vertices[vertice].previsit = clock.previsit()
        for x in range(0,len(self.ladjacent[vertice-1])):
            if self.vertices[self.ladjacent[vertice-1][x]].visited == False:
                self.explore2(self.ladjacent[vertice-1][x],clock)
            else:
                if self.vertices[self.ladjacent[vertice-1][x]].postvisit == None and self.vertices[self.ladjacent[vertice-1][x]].previsit != None:
                    self.circular = 1
                    
        self.vertices[vertice].postvisit = clock.postvisit()
        

    def cicle(self):
        clock = order()
        for x in range(1,len(self.ladjacent)+1):
            if self.vertices[x].visited == False:
                self.explore2(x,clock)
                if self.circular == 1:
                    break
    def sorting(self):
        clock = order()
        vertes = [y for x, y in sorted(zip(self.ladjacent,list(range(1,len(self.ladjacent)+1))), key=lambda pair: len(pair[0]),reverse=True)]
        for x in vertes:
            if self.vertices[x].visited == False:
                self.explore2(x,clock)    
        vertePost = [[x,self.vertices[x].postvisit] for x in  self.vertices.keys()]
        
        vertePost.sort(key=lambda x: x[1],reverse=True)

        
        return([x[0] for x in vertePost])



def main():
    features = [int(x) for x in input().split()]
    grafo = graph(features[0])
    for x in range(0,features[1]):
        n = [int(i) for i in input().split()]
       
        grafo.addedge_direct(n[0],n[1])
    j = grafo.sorting()
    print(*j, sep= " ")


    
        
    



if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()