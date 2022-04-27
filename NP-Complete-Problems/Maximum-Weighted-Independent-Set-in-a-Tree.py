#Python3
import sys
import threading

class vertex:
    def __init__(self):
        self.connections = []
        self.value_sub = float("inf")
        self.value = None
        self.root = False
        self.visited = False
        self.hijos = []

class graph:
    def __init__(self,vertexes):
        self.vertices = {x:vertex() for x in range(1,vertexes+1)}
        self.root = None
    def add_edge(self, v1, v2):
        if v1 not in self.vertices[v2].connections:
            self.vertices[v2].connections.append(v1)
            
        if v2 not in self.vertices[v1].connections:
            self.vertices[v1].connections.append(v2)    
    def add_values_root(self, dictvalues):
        for vertice in self.vertices.keys():
            self.vertices[vertice].value = dictvalues[vertice]
        for vertice in self.vertices.keys():
            if len(self.vertices[vertice].connections) <= 1:
                self.vertices[vertice].root = True
                self.root = vertice
                break
    def gerarquization(self,v):
        self.vertices[v].visited = True
        for vertice in self.vertices[v].connections:
            if self.vertices[vertice].visited == False: 
                self.gerarquization(vertice)
                self.vertices[v].hijos.append(vertice)
    def funparty(self,v):
        if self.vertices[v].value_sub == float("inf"):
            if len(self.vertices[v].hijos) == 0:
                self.vertices[v].value_sub = self.vertices[v].value
            else:
                m1 = self.vertices[v].value
                for hijo in self.vertices[v].hijos:
                    for nieto in self.vertices[hijo].hijos:
                        m1 = m1 + self.funparty(nieto)
                m0 = 0
                for hijo in self.vertices[v].hijos:
                    m0 = m0 + self.funparty(hijo)
                self.vertices[v].value_sub = max([m0,m1])
        return(self.vertices[v].value_sub)

def main():
    vertices = int(input())
    values = [int(x) for x in input().split()]
    values_dict = {x+1:values[x] for x in range(0,len(values))}
    grafo = graph(vertices)
    for x in range(0,vertices-1):
        n = [int(x) for x in input().split()]
        grafo.add_edge(n[0],n[1])
    grafo.add_values_root(values_dict)
    grafo.gerarquization(grafo.root)
    j = grafo.funparty(grafo.root)
    print(j)




if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()