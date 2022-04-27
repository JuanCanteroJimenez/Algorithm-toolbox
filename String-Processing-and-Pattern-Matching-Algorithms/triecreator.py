#Python3


class node:
    def __init__(self,key):
        self.key = key
        self.connections = []
        
        self.map_w_v = {}
class trie:
    def __init__(self):
        self.vertex = {0:node(0)}
        self.edges = []
    def add_edge_w(self, v1,v2,w):
        self.vertex[v2] = node(v2)
        
        self.vertex[v1].map_w_v[w] = v2
        
        self.vertex[v1].connections.append([v2,w])
        
        self.edges.append([v1,v2,w])
    def trieConstruction(self, patterns):
        index = 0
        for pattern in patterns:
            currentNode = self.vertex[0].key
            for i in range(0,len(pattern)):
                currentSymbol = pattern[i]
                if currentSymbol in self.vertex[currentNode].map_w_v:
                    currentNode = self.vertex[currentNode].map_w_v[currentSymbol]
                else:
                    index += 1
                    self.add_edge_w(currentNode,index,currentSymbol)
                    currentNode = index

def main():
    n = int(input())
    patterns = []
    for x in range(0,n):
        pattern = str(input())
        patterns.append(pattern)
    arbolito = trie()
    arbolito.trieConstruction(patterns)
    for edge in arbolito.edges:
        print("{}->{}:{}".format(edge[0],edge[1],edge[2]))

if __name__ == "__main__":
    main()



    
