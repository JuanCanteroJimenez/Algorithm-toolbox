#Python3

import sys
import threading

class tree:
    def __init__(self,key):
        self.key = key
        self.right = None
        self.left = None
        self.parent = None
        self.Height = None
    def isat2(self):
        results = []
        inordertrasversal(self,results)
        
        if results == sorted(results):
            print("CORRECT")
        else:
            print("INCORRECT")

def createtree(nodes,start):
    node = tree(nodes[start][0])
    if nodes[start][1] == -1 and nodes[start][2] == -1:
        return(node)   
    else:
        if nodes[start][1] != -1:
            node.left = createtree(nodes,nodes[start][1])
        if nodes[start][2] != -1:
            node.right = createtree(nodes,nodes[start][2])
        return(node)

def inordertrasversal(tree,lista):
    if tree == None :
        
        return()
    inordertrasversal(tree.left,lista)
    lista.append(tree.key)
    inordertrasversal(tree.right,lista)

    

def main():
    n = int(input())
    if n == 0:
        print("CORRECT")
        return()
    nodes = []
    for x in range(0,n):
        nodo = [int(j) for j in input().split()]
        nodes.append(nodo)

    j = createtree(nodes,0)
    
    j.isat2()


if __name__ == "__main__":
    sys.setrecursionlimit(10**7)  # max depth of recursion
    threading.stack_size(2**27)   # new thread will get stack of such size
    threading.Thread(target=main).start()
