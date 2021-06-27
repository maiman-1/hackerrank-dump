class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def preOrder(root):
    #Write your code here
    q = []
    q.append(root.info)
    if root.left is not None:
        preOrder_aux(root.left, q)
    if root.right is not None:
        preOrder_aux(root.right, q)
    #print(q)
    while len(q) > 0:
        print(q.pop(0), end=" ")
    
    
def preOrder_aux(current: Node, q: list):
    #print(current.info)
    q.append(current.info)
    if current.left is not None:
        preOrder_aux(current.left, q)
    if current.right is not None:
        preOrder_aux(current.right, q)



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

preOrder(tree.root)