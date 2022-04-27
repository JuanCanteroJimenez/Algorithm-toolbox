#Python3
import sys
import threading
from collections import deque
import heapq
import time
import math

from collections import defaultdict
from typing import Any
from typing import DefaultDict
from typing import Generic
from typing import Iterator
from typing import Set
from typing import Tuple
from typing import TypeVar
from typing import Union

from typing import Dict
from typing import TypeVar

T = TypeVar("T")


class IdentityDict(Dict[T, T]):
    """A defaultdict implementation which places the requested key as its value in case it's missing."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __missing__(self, key: T) -> T:
        self[key] = key
        return key

T = TypeVar("T")


class InvalidInitialMappingError(RuntimeError):
    """Runtime error raised when invalid initial mapping causes the find() methods to change during iteration."""

    def __init__(
        self,
        msg=(
            "The mapping passed during ther DisjointSet initialization must have been wrong. "
            "Check that all keys are mapping to other keys and not some external values."
        ),
        *args,
        **kwargs,
    ):
        super().__init__(msg, *args, **kwargs)


class DisjointSet(Generic[T]):
    """A disjoint set data structure."""

    def __init__(self, *args, **kwargs) -> None:
        self._data: IdentityDict[T] = IdentityDict(*args, **kwargs)

    def __contains__(self, item: T) -> bool:
        return item in self._data

    def __bool__(self) -> bool:
        return bool(self._data)

    def __get__(self, element: T) -> T:
        return self.find(element)

    def __eq__(self, other: Any) -> bool:
        """
        Return True if both DistjoinSet structures are equivalent.
        This may mean that their canonical elements are different, but the sets they form are the same.
        >>> DisjointSet({1: 1, 2: 1}) == DisjointSet({1: 2, 2: 2})
        True
        """
        if not isinstance(other, DisjointSet):
            return False

        return {tuple(x) for x in self.itersets()} == {tuple(x) for x in other.itersets()}

    def __repr__(self) -> str:
        """
        Print self in a reproducible way.
        >>> DisjointSet({1: 2, 2: 2})
        DisjointSet({1: 2, 2: 2})
        """
        sets = {key: val for key, val in self}
        return f"{self.__class__.__name__}({sets})"

    def __str__(self) -> str:
        return "{classname}({values})".format(
            classname=self.__class__.__name__, values=", ".join(str(dset) for dset in self.itersets()),
        )

    def __iter__(self) -> Iterator[Tuple[T, T]]:
        """Iterate over items and their canonical elements."""
        try:
            for key in self._data.keys():
                yield key, self.find(key)
        except RuntimeError as e:
            raise InvalidInitialMappingError() from e

    def itersets(self, with_canonical_elements: bool = False) -> Iterator[Union[Set[T], Tuple[T, Set[T]]]]:
        """
        Yield sets of connected components.
        If with_canonical_elements is set to True, method will yield tuples of (<canonical_element>, <set of elements>)
        >>> ds = DisjointSet()
        >>> ds.union(1,2)
        >>> list(ds.itersets())
        [{1, 2}]
        >>> list(ds.itersets(with_canonical_elements=True))
        [(2, {1, 2})]
        """
        element_classes: DefaultDict[T, Set[T]] = defaultdict(set)
        for element in self._data:
            element_classes[self.find(element)].add(element)

        if with_canonical_elements:
            yield from element_classes.items()
        else:
            yield from element_classes.values()

    def find(self, x: T) -> T:
        """
        Return the canonical element of a given item.
        In case the element was not present in the data structure, the canonical element is the item itself.
        >>> ds = DisjointSet()
        >>> ds.find(1)
        1
        >>> ds.union(1, 2)
        >>> ds.find(1)
        2
        """
        while x != self._data[x]:
            self._data[x] = self._data[self._data[x]]
            x = self._data[x]
        return x

    def union(self, x: T, y: T) -> None:
        """
        Attach the roots of x and y trees together if they are not the same already.
        :param x: first element
        :param y: second element
        """
        parent_x, parent_y = self.find(x), self.find(y)
        if parent_x != parent_y:
            self._data[parent_x] = parent_y

    def connected(self, x: T, y: T) -> bool:
        """
        Return True if x and y belong to the same set (i.e. they have the canonical element).
        >>> ds = DisjointSet()
        >>> ds.connected(1, 2)
        False
        >>> ds.union(1, 2)
        >>> ds.connected(1, 2)
        True
        """
        return self.find(x) == self.find(y)
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
        self.ladjacent_0w = [[] for x in range(0,vertexs)]
        self.vertices = {x:vertex() for x in range(1,vertexs+1)}
        self.edges = []
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
    def addedge_weighted(self,v1,v2,v3):

        if v2  not in self.ladjacent_0w[v1-1]:
            self.ladjacent[v1-1].append((v2,v3))
            self.ladjacent_0w[v1-1].append(v2)
        if v1  not in self.ladjacent_0w[v2-1]:
            self.ladjacent[v2-1].append((v1,v3))
            self.ladjacent_0w[v2-1].append(v1)

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
    
    def make_graph(self, list_of_points):
        referencias = { x+1:[list_of_points[x]] for x in range(0,len(list_of_points))}
        for x in referencias.keys():
            for i in referencias.keys():
                source = x
                target = i
                referencias[x]
                if source != target:
                    h =  ((referencias[x][0][0]-referencias[i][0][0])**2) + ((referencias[x][0][1] - referencias[i][0][1])**2 )
                    
                    weight = math.sqrt(h)
                    self.addedge_weighted(source,target,weight)
                    self.edges.append([source,target,weight])
    
    def krustal(self):
        list_of_edges = self.edges
        list_of_edges.sort(key = lambda x: x[2])
        new_graph = []
        ds = DisjointSet()
        path_value = 0
        stoping = len(list(self.vertices.keys())) - 1
        [ds.find(x) for x in self.vertices.keys()]
        for x in list_of_edges:
            if ds.connected(x[0],x[1]) == False:
                new_graph.append(x)
                ds.union(x[0],x[1])
                path_value += x[2]
                if len(new_graph) == stoping:
                    break
        return(path_value, new_graph)



def main():

    puntos = int(input())
    grafo = graph(puntos)
    list_of_points = []
    for _ in range(0,puntos):
        n = [int(x) for x in input().split()]
        list_of_points.append(n)
    grafo.make_graph(list_of_points)
    distancia, nuevo_grafo = grafo.krustal()
    print(round(distancia,9))

    pass

if __name__ == "__main__":
    main()