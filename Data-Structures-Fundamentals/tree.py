#Python3
import sys
import threading

class TreeNode: 
    def __init__(self, data): 
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level1(self):

        if self.children:
            levels = []
            for child in self.children:
                levels.append(child.get_level1())
            return(1 + max(levels))

                
        else: 
            return(1)

    def subtree(self, node):
        if self.children:
    
            for child in self.children: 
                if child == node:
                    return(child)
                else: 
                    child.subtree(node)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + str(self.data))
        if self.children:
            for child in self.children:
                child.print_tree()

def create_tree(nodos, raiz):
    
        
    if raiz in nodos:
    
        for x in range(0,len(nodos)):
            
            if nodos[x] == raiz and raiz == -1:
                
                raiztree = TreeNode(x)
                hijo = create_tree(nodos, x)
                
                raiztree.add_child(hijo)
            elif nodos[x] == raiz:
                hijo = create_tree(nodos, x)
                return(hijo)  
        if raiz == -1:      
            return(raiztree)  
        
                    
    else: 
        m = TreeNode(nodos[raiz])
        
        m.add_child(TreeNode(raiz))
        
        
        return(m)
    
def create_tree2(nodos):
    dicti = {}
    for x in range(0,len(nodos)):
        dicti.update({x:TreeNode(x)})
    for x in range(0,len(nodos)):
        if nodos[x] == -1:
            root = x
        else:
            dicti[nodos[x]].add_child(dicti[x]) 
    return(dicti[root])


def main():

    n = int(input())
    nodes = [int(x) for x in input().split()]
    prueba = create_tree2(nodes)
    
    print(prueba.get_level1())

sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
