# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

import sys
sys.setrecursionlimit(10001)

root = None
        

class node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.p = None
        self.left = None
        self.right = None


def Inorder_Tree_Walk(x):
    if x != None:
        Inorder_Tree_Walk(x.left)
        print(x.key)
        Inorder_Tree_Walk(x.right)


def Tree_Minimum(x):
    while x.left is not None:
        x = x.left
    return x

def Tree_Maximum(x):
    while x.right is not None:
        x = x.right
    return x

def Tree_Successor(x):
    if x.right is not None:
        return Tree_Minimum(x.right)
    parent= x.p
    while parent is not None and x is parent.right:
        x = parent
        parent = parent.p
    return parent


def Tree_Predecessor(x):
    if x.left is not None:
        return Tree_Maximum(x.left)
    parent= x.p
    while parent is not None and x is parent.left:
        x = parent
        parent = parent.p
    return parent

'''
Adding your own Tree_Predecessor(x) is recommended, but not required
'''

def Transplant(u, v):
    global root
    if u.p is None:
        root = v
    elif u is u.p.left:
        u.p.left = v
    else:
        u.p.right = v
    if v is not None:
        v.p = u.p
    pass 

def Tree_Delete(z):
    if z.left is None:
        Transplant(z,z.right)
    elif z.right is None:
        Transplant(z,z.left)
    else:
        y = Tree_Minimum(z.right)

        if y.p is not z:
            
            Transplant(y,y.right)
            y.right = z.right
            y.right.p = y
        Transplant(z,y)
        y.left = z.left
        y.left.p = y  

def Tree_Search(k):
    global root
    x = root
    while x is not None and x.key != k:
        if x.key < k:
            x = x.right
        else:
            x = x.left
    return x

def Tree_Insert(root,z):
    parent = None
    x = root
    while x is not None:
        parent = x
        if z.key < x.key:
            x = x.left
        else:
            x = x.right
    z.p = parent
    if parent is None:
        x = z
    elif z.key < parent.key:
        parent.left = z
    else:
        parent.right = z

# Function to print
def printCall ( node , indent , last ) :
    if node != None :
        print(indent, end=' ')
        if last :
            print ("R----",end= ' ')
            indent += "     "
        else :
            print("L----",end=' ')
            indent += "|    "

        print ( str ( node.key ) )
        printCall ( node.left , indent , False )
        printCall ( node.right , indent , True )

def checkTree(root):
    if root is None:
        return True
    else:
        if root.p is not None:
            if root is root.p.left:
                if root.key < root.p.key:
                    return checkTree(root.left) and checkTree(root.right)
                else:
                    return False
            elif root is root.p.right:
                if root.key >= root.p.key:
                    return checkTree(root.left) and checkTree(root.right)
                else:
                    return False
        else:
            return checkTree(root.left) and checkTree(root.right)
        
# Function to call print
def print_BSTree (root) :
    printCall( root , "" , True )


data = [10,5,15,14,3,7,17]

root = node(20,None)
for x in data:
    Tree_Insert(root,node(x,None))

print_BSTree(root)
print(checkTree(root))
Tree_Delete(Tree_Search(10))
print_BSTree(root)


a,b = node(18,None), node(25,None)
c,d = node(28,None), node(11,None)
root2 = a
a.left = b
b.p = a
a.right = c
c.p = a
c.left = d
d.p = c
print_BSTree(root2)
print(checkTree(root2))

