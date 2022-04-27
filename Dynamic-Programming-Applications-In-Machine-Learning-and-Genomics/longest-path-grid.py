#Python3
import sys
import threading
from collections import deque
import heapq
import time
class vertice_dijkstra:
    def __init__(self,vertice,previo,distancia):
        self.previo = previo
        self.distancia = distancia
        self.vertice = vertice
        self.cambiado = False
    def __lt__(self,other):
        
        return(self.distancia < other.distancia)
    def __str__(self):
        return("vertice: %s, distancia: %s, previo: %s, visitado: %s"% (str(self.vertice),str(self.distancia),str(self.previo),str(self.cambiado)))

class vertex:
    def __init__(self):
        self.postvisit = None
        self.previsit = None
        self.visited = False
        self.level = -1
        self.distance = float("inf")
        self.prev = []
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
    def addedge_direct_weigthed(self,v1,v2,edge):
        if v2  not in self.ladjacent[v1-1]:
            self.ladjacent[v1-1].append((v2,edge))
          

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
    
    def distance(self,partida,llegada):
        q = deque()
        q.append(partida)
        self.vertices[partida].level = 0
        while len(q) != 0:
            u = q.popleft()
            for x in self.ladjacent[u-1]:
                if self.vertices[x].level == -1:
                    q.append(x)
                    self.vertices[x].level = self.vertices[u].level + 1
        return(self.vertices[llegada].level)

    def dijkstra(self, partida):
        referencias = {}
        
        for x in self.vertices.keys():
            if x == partida:
                referencias[x] = vertice_dijkstra(x,None,[0,x])
            else:
                referencias[x] = vertice_dijkstra(x,None,[float("inf"),x])
        H = [referencias[x] for x in referencias.keys()]
        heapq.heapify(H)
        while len(H) != 0:
            
            u = heapq.heappop(H)
            for v in self.ladjacent[u.vertice-1]:
                if referencias[v[0]].distancia[0] > referencias[u.vertice].distancia[0] + v[1]:
                    if len(H) != 0:
                        referencias[v[0]].distancia[0] = -1
                        heapq.heappush(H,vertice_dijkstra(0,0,[-1,0]))
                        heapq.heappop(H)
                        heapq.heappop(H)
                        referencias[v[0]].distancia[0] = referencias[u.vertice].distancia[0] + v[1]
                        referencias[v[0]].previo = u.vertice
                        heapq.heappush(H,referencias[v[0]])
                    else:
                        referencias[v[0]].distancia[0] = referencias[u.vertice].distancia[0] + v[1]
                        referencias[v[0]].previo = u.vertice

                    
        return(referencias)

    def dijkstra1(self, partida):
            referencias = {}
            
            for x in self.vertices.keys():
                if x == partida:
                    referencias[x] = vertice_dijkstra(x,None,[0,x])
                else:
                    referencias[x] = vertice_dijkstra(x,None,[float("inf"),x])
            H = [referencias[x] for x in referencias.keys()]
            heapq.heapify(H)
            while len(H) != 0:
                p = 0
                while p == 0:
                    
                    u = heapq.heappop(H)
                    if len(H) == 0:
                        p = 1
                    if u.cambiado == False:
                        p = 1
                    
                
                for v in self.ladjacent[u.vertice-1]:
                    if referencias[v[0]].distancia[0] > referencias[u.vertice].distancia[0] + v[1]:
                        referencias[v[0]].distancia[0] = referencias[u.vertice].distancia[0] + v[1]
                        referencias[v[0]].previo = u.vertice
                        referencias[v[0]].cambiado = False
                        t = vertice_dijkstra(referencias[v[0]].vertice,referencias[v[0]].previo,referencias[v[0]].distancia)
                        heapq.heappush(H,t)
                        referencias[v[0]].cambiado = True
                        
            return(referencias)

    def BelmanFord(self, partida):
        referencias = {}
        
        for x in self.vertices.keys():
            if x == partida:
                referencias[x] = vertice_dijkstra(x,None,0)

            else:
                referencias[x] = vertice_dijkstra(x,None,223372036854775807)
        
        z = 0
        control = True
        while control:
            for x in range(0,len(self.ladjacent)):
                for y in self.ladjacent[x]:
                    if referencias[y[0]].distancia > referencias[x+1].distancia + y[1]:
                        referencias[y[0]].distancia = referencias[x+1].distancia + y[1]
                        referencias[y[0]].previo = x+1


            
            if z == (len(list(self.vertices.keys()))):
                control = False
            z += 1
            
        for x in range(0,len(self.ladjacent)):
            for y in self.ladjacent[x]:
                if referencias[y[0]].distancia > referencias[x+1].distancia + y[1]:
                    j = referencias[y[0]]
                    h = j
                    for _ in range(0,len(self.ladjacent)):
                        h = referencias[h.previo]
                        if h.vertice == j.vertice:
                            return(1)
                        elif h.previo == None:
                            return(0)
                    return(1)

                    
        
        return(0)

    def BelmanFord2(self, destino):
            partida = 1
            referencias = {}
            
            for x in self.vertices.keys():
                if x == partida:
                    referencias[x] = vertice_dijkstra(x,None,0)

                else:
                    referencias[x] = vertice_dijkstra(x,None,223372036854775807)
            
            z = 0
            control = True
            while control:
                for x in range(0,len(self.ladjacent)):
                    for y in self.ladjacent[x]:
                        if referencias[y[0]].distancia > referencias[x+1].distancia + y[1]:
                            referencias[y[0]].distancia = referencias[x+1].distancia + y[1]
                            referencias[y[0]].previo = x+1


                
                if z == (len(list(self.vertices.keys()))):
                    control = False
                z += 1
            pass
            """   
            for x in range(0,len(self.ladjacent)):
                for y in self.ladjacent[x]:
                    if referencias[y[0]].distancia > referencias[x+1].distancia + y[1]:
                        j = referencias[y[0]]
                        h = j
                        for _ in range(0,len(self.ladjacent)):
                            h = referencias[h.previo]
                            if h.vertice == j.vertice:
                                return(1)
                            elif h.previo == None:
                                return(0)
                        return(1)

                        
            """
            return(referencias[destino].distancia*-1)





    
    



def main():
    features = [int(x)+1 for x in input().split()]
    grafo = graph(features[0]*features[1])
    down = []
    side = []
    
    for _ in range(0,features[0]-1):
        down.append([int(x)*-1 for x in input().split()])
    input()
    
    for _ in range(0,features[0]):
        side.append([int(x)*-1 for x in input().split()])
    
    for x in range(0,len(down)):
        for y in range(0,len(down[x])):
            v = y + 1 + x*len(down[x])
            u = y + 1 + (x+1)*len(down[x])
            grafo.addedge_direct_weigthed(v, u, down[x][y])
    
    for x in range(0,len(side)):
        for y in range(0,len(side[x])):
            v = y + 1 + x*(len(side[x])+1)
            u = v + 1 
            grafo.addedge_direct_weigthed(v, u, side[x][y])
    
    
    j = grafo.BelmanFord2(features[0]*features[1])
    print(j)
   

    
    
    


    
        
    



if __name__ == "__main__":
    main()