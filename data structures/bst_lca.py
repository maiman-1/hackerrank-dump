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

# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    # From geeks4geeks
    # step 1 find a  path from root to v1
    path1 = []
    findPaths(root, path1, v1)
    #print(path1)
    path2 = []
    findPaths(root, path2, v2)
    #print(path2)
    lca = None
    i = 0
    j = 0
    while i < len(path1) and j < len(path2):
        if path1[i] == path2[j]:
            lca = path1[i]
        i += 1
        j += 1
    return lca

def findPaths(current, paths, value):
    # Base case is when the node is None
    if current is None:
        return False
    else:
        # Append first
        paths.append(current)
        
        # check if the value matches
        if current.info == value:
            return True
        if (current.left is not None and findPaths(current.left, paths, value)) or      (current.right is not None and findPaths(current.right, paths, value)):
            return True
        
        # if all of these fail, the paths does not contain the value
        paths.pop()
        return False
        
        

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print (ans.info)
