#Python3
import itertools
import json
import sys
import threading

def varnum(vertice, value):
    return(vertice*10+value)
def varnum2(literal):
    if literal < 0:
        return(varnum(literal*-1,0))
    else:
        return(varnum(literal,1))

class vertex:
    def __init__(self):
        self.preorder = None
        self.postorder = None
        self.visited = False
        self.stronglycc = None
        self.target = []
        self.eliminated = False
        self.value = None
        
class edge:
    def __init__(self,source_e,target_e):
        self.source = source_e
        self.target = target_e
        self.weight = None

class order:
    def __init__(self):
        
        self.clock = 0
    def previsit(self):
        self.clock += 1
        return(self.clock)
    def postvisit(self):
        self.clock += 1
        return(self.clock)


class graph_implication:
    def __init__(self,variables):
        self.variables = variables
        self.vertices = {varnum(x,y):vertex() for x,y in itertools.product(range(1,variables+1),[0,1])}
        self.vertices_r = {varnum(x,y):vertex() for x,y in itertools.product(range(1,variables+1),[0,1])}
        self.edges = {}
        self.edges_r = {}
        self.edge_counter = 0
        self.edge_counter_r = 0
        self.n_scc = 0
        self.valido = True
    def add_edge_directed(self,source,target_v):
        if target_v not in self.vertices[source].target:
            self.vertices[source].target.append(target_v)
            self.edges[self.edge_counter+1] = edge(source,target_v)
            self.edge_counter += 1
        if source not in self.vertices_r[target_v].target:
            self.vertices_r[target_v].target.append(source)
            self.edges_r[self.edge_counter_r+1] = edge(target_v,source)
            self.edge_counter_r +=1
    def explore(self,v,clock):
        self.vertices[v].visited = True
        self.vertices[v].preorder = clock.previsit()
        for target in self.vertices[v].target:
            if self.vertices[target].visited == False:
                self.explore(target,clock)
        self.vertices[v].postorder = clock.postvisit()
    def explore2(self,v,scc):
        self.vertices[v].visited = True
        self.vertices[v].eliminated = True
        self.vertices[v].stronglycc = scc
        for target in self.vertices[v].target:
            if self.vertices[target].visited == False and self.vertices[target].eliminated == False:
                self.explore2(target,scc)
    
    def explore_vlogical(self,v,literals):
        self.vertices[v].visited = True
        previo = None
        for target in self.vertices[v].target:
            if self.vertices[target].visited == False:
                previo=self.explore_vlogical(target,literals)
        if literals[v//10][1] == None:
            if v%10 == 0:
                literals[v//10][1] = 0
                
            else:
                literals[v//10][1] = 1
        else:
            if v%10 == 0 and literals[v//10][1] == 1:
                self.vertices[v].value = False
            elif v%10 == 0 and literals[v//10][1] == 0:
                self.vertices[v].value = True
            elif v%10 == 1 and literals[v//10][1] == 0:
                self.vertices[v].value = False
            elif v%10 == 1 and literals[v//10][1] == 1:
                self.vertices[v].value = True
        if previo == False and self.vertices[v].value ==True:
            self.valido = False
        return(self.vertices[v].value)
                
        
    def explore_vlogical2(self,v,literals):
        self.vertices[v].visited = True
        for target in self.vertices[v].target:
            if self.vertices[target].visited == False:
                self.explore_vlogical2(target,literals)
        if literals[v//10][1] == None:
            if v%10 == 0:
                literals[v//10][1] = 0
            else:
                literals[v//10][1] = 1
        else:
            if v%10 == 0 and literals[v//10][1] == 1:
                self.valido = False
            if v%10 == 1 and literals[v//10][1] == 0:
                self.valido = False
        

            

        
    def dfs(self):
        clock = order()
        for v in self.vertices.keys():
            if self.vertices[v].visited == False:
                self.explore(v,clock)
    def reverse(self):
        grafo_reverse = graph_implication(self.variables)
        grafo_reverse.vertices = self.vertices_r
        grafo_reverse.edges = self.edges_r
        return(grafo_reverse)
    def SCCs (self):
        grafo_reverse = self.reverse()
        grafo_reverse.dfs()
        ordered = sorted(grafo_reverse.vertices.items(),key= lambda x: x[1].postorder,reverse=True)
        number = 0
        for v in ordered:
            
            if self.vertices[v[0]].visited==False:
                number += 1
                self.explore2(v[0],number)
                
            else:
                pass
        self.n_scc = number
    def plotting_bonito(self):
        to_json = {"nodes":[],"links":[]}
        for vertice in self.vertices.keys():
            if self.vertices[vertice].stronglycc:

                to_json["nodes"].append({"name":str(vertice), "id":str(self.vertices[vertice].stronglycc), "age":"20"})
            else:
                to_json["nodes"].append({"name":str(vertice), "id":"1", "age":"20"})
        for edge in self.edges.keys():
            to_json["links"].append({"source":str(self.edges[edge].source),"target":str(self.edges[edge].target),"value":10,"stroke":1})
        with open("data.json","w") as f:
            json.dump(to_json, f, sort_keys=True, indent=4)

    def sat2(self):
        literalas = {x:[None,None] for x in range(1,self.variables+1)}
        
        self.SCCs()
        
        for vertice_l in self.vertices.keys():
            vertice = vertice_l // 10
            if literalas[vertice][0] == None:
                literalas[vertice][0] = self.vertices[vertice_l].stronglycc
            elif literalas[vertice][0] == self.vertices[vertice_l].stronglycc:

                print("UNSATISFIABLE")
                return()
            else:
                pass
        sccs = {}
        for vertice in self.vertices.keys():
            if self.vertices[vertice].stronglycc in sccs:
                
                sccs[self.vertices[vertice].stronglycc][vertice] = self.vertices[vertice]
            else:
                sccs[self.vertices[vertice].stronglycc] = {}
                sccs[self.vertices[vertice].stronglycc][vertice] = self.vertices[vertice]
        for vertice in self.vertices.keys():
            self.vertices[vertice].visited = False
        self.valido = True
        for scc in range(len(list(sccs.keys())),0,-1):
            inicio = list(sccs[scc].keys())[0]
            self.explore_vlogical(inicio, literalas)
            
        print("SATISFIABLE")     
        resultados = [x*-1 if literalas[x][1] == 0 else x for x in literalas.keys() ]
        print(*resultados)
            



            



        
        



def main():
    features = [int(x) for x in input().split()]
    grafo = graph_implication(features[0])
    for x in range(0,features[1]):
        n = [int(i) for i in input().split()]
        if len(n) == 1:
            
            grafo.add_edge_directed(varnum2(n[0]*-1),varnum2(n[0]))
            
        else:
            grafo.add_edge_directed(varnum2(n[0]*-1),varnum2(n[1]))
            grafo.add_edge_directed(varnum2(n[1]*-1),varnum2(n[0]))
    
    j = grafo.sat2()
    
    
    
        

        
if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()