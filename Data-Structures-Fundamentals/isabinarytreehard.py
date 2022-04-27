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
        results2 = []
        isatree2(self,results2)
        inordertrasversal(self,results)
        
        if results == sorted(results) and sum(results2) == 0:
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

def isatree2(tree,lista):
    if tree == None:
        return()
    if tree.left is not None and tree.left.key < tree.key:
        lista.append(0)
    elif tree.left is not None and tree.left.key >= tree.key:
        lista.append(1)
        return()
    if tree.right is not None and tree.right.key >= tree.key:
        lista.append(0)
    elif tree.right is not None and tree.right.key < tree.key:
        lista.append(1)
        return()
    isatree2(tree.left,lista)
    isatree2(tree.right,lista)

    

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
