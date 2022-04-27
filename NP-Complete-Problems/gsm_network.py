#Python3
import sys
import threading
from collections import deque
import heapq
import time
import itertools
import os
import json
from collections import Counter

def exactly_one_of(literals,clauses):
    
    clauses.append([l for l in literals])

    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])
      

def varnum(vertex, color):
    return(vertex*10 + color)

class verticestt:
    def __init__(self,inicio):
        self.numero = inicio
    def uno_mas(self):
        self.numero += 1
        return(self.numero)
    
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
        self.color = None
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
        self.edges = []
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
    def gsm(self):
        colores = [1,2,3]
        diccionario = {}
        clauses = []
        dicc_redundacia = {}
        z = 1
        for vertex in self.vertices.keys():
            for color in colores:
                diccionario[varnum(vertex,color)] = z
                dicc_redundacia[vertex] = []
                z += 1

        
        for vertex in range(0, len(self.ladjacent) ):
            
            exactly_one_of([varnum(vertex+1, color) for color in colores],clauses)
        filtro_redundacia = []
        for vertices in range(0,len(self.ladjacent)):
            vertice = vertices + 1
            
            for vecino in self.ladjacent[vertices]:
                control = 0
                if vertice in dicc_redundacia[vecino] or vecino in dicc_redundacia[vertice]:
                    control = 1
                    

                if control == 0:
                    for color in colores:
                        clauses.append([-(varnum(vertice,color)), -(varnum(vecino,color))]) 
                    dicc_redundacia[vertice].append(vecino)
                    dicc_redundacia[vecino].append(vertice)



        clauses_limpio = []
        for clause in clauses:
            i = []
            for element in clause:
                if element < 0:
                    i.append(-diccionario[element*-1])
                else:
                    i.append(diccionario[element])
            clauses_limpio.append(i)

        
        clauses_flat = [item for sublist in clauses_limpio for item in sublist]
        j = max(clauses_flat,key=abs)
        if j < 0:
            j = j*-1

        print("{} {}".format(len(clauses_limpio),j))
        for c in clauses_limpio:
                c.append(0)
                print(" ".join(map(str, c)))
        

        
        """
        with open('tmp.cnf', 'w') as f:
            f.write("p cnf {} {}\n".format(j, len(clauses_limpio)))
            for c in clauses_limpio:
                
                f.write(" ".join(map(str, c))+"\n")
        
        os.system("minisat tmp.cnf tmp.sat")
        with open("tmp.sat", "r") as satfile:
            for line in satfile:
                if line.split()[0] == "UNSAT":
                    print("There is no solution")
                elif line.split()[0] == "SAT":
                    pass
                else:
                    assignment = [str(x) for x in line.split()]
                    for j in assignment:
                        if "-" in j:
                            pass
                        elif len(j) == 1:
                            pass
                        elif len(j) == 2 and "0" in j:
                            pass
                        else:
                            a = int(j[0:len(j)-1])
                            b = max(list(self.vertices.keys()))
                            
                            if a in list(self.vertices.keys()):
                                color = j[len(j)-1]
                                vertice = j[0:len(j)-1]
                                #print("Vertice:",vertice,"tiene el color",colores_dict[int(color)])

                                self.vertices[int(vertice)].color = int(color)
                            
                                
                            
    

        return(clauses)
        """
    def plotting_bonito(self):
        to_json = {"nodes":[],"links":[]}
        for vertice in self.vertices.keys():
            if self.vertices[vertice].color:

                to_json["nodes"].append({"name":str(vertice), "id":str(self.vertices[vertice].color), "age":"20"})
            else:
                to_json["nodes"].append({"name":str(vertice), "id":"1", "age":"20"})
        for edge in self.edges:
            to_json["links"].append({"source":str(edge[0]),"target":str(edge[1]),"value":10})
        with open("data.json","w") as f:
            json.dump(to_json, f, sort_keys=True, indent=4)

    def simplify(self):
        diccionario = {}
        posicion = 1
        eliminados = []
        for x in range(0,len(self.ladjacent)):
            if len(self.ladjacent[x]) <= 2:
                eliminados.append(x+1)
            else:
                diccionario[x+1] = posicion
                posicion += 1
        if len(eliminados) == 0:
            return(self)
        else:
            edges_limpio = []
            for x in self.edges:
                if x[0] in eliminados or x[1] in eliminados:
                    pass
                else:
                    edges_limpio.append([diccionario[x[0]],diccionario[x[1]]])
            h = graph(posicion)
            for edge in edges_limpio:
                h.addedge(edge[0],edge[1])
                h.edges.append([edge[0],edge[1]])
            return(h)




            






        
            

    
    
def main():
    features = [int(x) for x in input().split()]
    grafo = graph(features[0])
    for x in range(0,features[1]):
        
        n = [int(i) for i in input().split()]
        
        grafo.addedge(n[0],n[1])
        grafo.edges.append([n[0],n[1]])
    
    grafo.gsm()
    
    



    
    


    
        
    



if __name__ == "__main__":
    main()
    