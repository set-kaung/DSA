# Define Node
import random


class RB_Node():
    def __init__(self,key, data=None):
        self.data = data
        self.key = key                                   # Key of Node
        self.p = None                                    # Parent of Node
        self.left = None                                 # Left Child of Node
        self.right = None                                # Right Child of Node
        self.color = 1                                   # Red Node as new node is always inserted as Red Node

# Define R-B Tree
class RBTree():
    def __init__(self):
        self.NULL = RB_Node ( 0 )
        self.NULL.color = 0
        self.NULL.left = None
        self.NULL.right = None
        self.root = self.NULL


    # Insert New Key
    def insert(self, key):
        node = RB_Node(key)
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        self.RB_Insert(node)

    # Insert New Node
    def RB_Insert(self, node):
        node.p = None
        node.left = self.NULL
        node.right = self.NULL
        node.color = 1                                   # Set root colour as Red
        
        y = None
        x = self.root

        # because of the loop's behavior, y is set as just before
        # the place to insert z, aka y is z's potential parent
        while x != self.NULL :                           # Find position for new node
            y = x
            if node.key < x.key :
                x = x.left
            else :
                x = x.right

        node.p = y                                       # Set p of Node as y
        if y == None :                                   # If parent i.e, is none then it is root node
            self.root = node
        elif node.key < y.key :                          # Check if it is right Node or Left Node by checking the value
            y.left = node
        else :
            y.right = node

        if node.p == None :                              # Root node is always Black
            node.color = 0
            return

        if node.p.p == None :                            # If parent of node is Root Node
            return

        self.fixInsert ( node )                          # Else call for Fix Up


    def Tree_Minimum(self, node):
        if node == None:
            return
        while node.left != self.NULL:
            node = node.left
        return node

    def Tree_Maximum(self, node):
        while node.right != self.NULL:
            node = node.right
        return node

    # Code for left rotate
    def LR(self, x):
        y = x.right  # y is the right child of x
        x.right = y.left  # Set x's right child to y's left child

        if y.left != self.NULL:  # If y's left child is not NULL
            y.left.p = x  # Set the parent of y's left child to x

        y.p = x.p  # Set y's parent to x's parent
        if x.p == None:  # If x is the root
            self.root = y  # Set y as the new root
        elif x == x.p.left:  # If x is the left child of its parent
            x.p.left = y  # Set y as the new left child of x's parent
        else:  # If x is the right child of its parent
            x.p.right = y  # Set y as the new right child of x's parent

        y.left = x  # Set x as the left child of y
        x.p = y  # Set y as the parent of x



    # Code for right rotate
    def RR(self, x):
        y = x.left                                       # Y = Left child of x
        x.left = y.right                                 # Change left child of x to right child of y
        if y.right != self.NULL:
            y.right.p = x                               # Update parent of y.right

        y.p = x.p                                        # Change parent of y to parent of x
        if x.p is None:                                  # If x is the root node
            self.root = y                               # Set y as the new root
        elif x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y

        y.right = x                                      # Make x the right child of y
        x.p = y                                          # Update parent of x



    # Fix Up Insertion
    def fixInsert(self, k):
        while k.p.color == 1:                            # While parent is red
            if k.p == k.p.p.right:                       # if parent is right child of its parent
                u = k.p.p.left                           # Left child of grandparent
                if u.color == 1:                         # if color of left child of grandparent i.e, uncle node is red
                    u.color = 0                          # Set both children of grandparent node as black
                    k.p.color = 0
                    k.p.p.color = 1                      # Set grandparent node as Red
                    k = k.p.p                            # Repeat the algo with Parent node to check conflicts
                else:
                    if k == k.p.left:                    # If k is left child of it's parent
                        k = k.p
                        self.RR(k)                       # Call for right rotation
                    k.p.color = 0
                    k.p.p.color = 1
                    self.LR(k.p.p)
            else:                                         # if parent is left child of its parent
                u = k.p.p.right                           # Right child of grandparent
                if u.color == 1:                          # if color of right child of grandparent i.e, uncle node is red
                    u.color = 0                           # Set color of childs as black
                    k.p.color = 0
                    k.p.p.color = 1                       # set color of grandparent as Red
                    k = k.p.p                             # Repeat algo on grandparent to remove conflicts
                else:
                    if k == k.p.right:                    # if k is right child of its parent
                        k = k.p
                        self.LR(k)                        # Call left rotate on parent of k
                    k.p.color = 0
                    k.p.p.color = 1
                    self.RR(k.p.p)                        # Call right rotate on grandparent
            if k == self.root:                            # If k reaches root then break
                break
        self.root.color = 0                               # Set color of root as black


    # Function to fix issues after deletion
    def fixDelete(self, x):
        while x != self.root and x.color == 0:  # Repeat until x reaches root and color of x is black
            if x == x.p.left:  # If x is left child of its parent
                s = x.p.right  # Sibling of x
                if s.color == 1:  # If sibling is red
                    s.color = 0  # Set sibling's color to black
                    x.p.color = 1  # Make parent's color red
                    self.LR(x.p)  # Call left rotation on parent
                    s = x.p.right  # Update sibling
                # If both children of sibling are black
                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1  # Set sibling's color to red
                    x = x.p  # Move x up to parent
                else:
                    if s.right.color == 0:  # If right child of sibling is black
                        s.left.color = 0  # Set left child of sibling to black
                        s.color = 1  # Set sibling's color to red
                        self.RR(s)  # Call right rotation on sibling
                        s = x.p.right  # Update sibling after rotation

                    s.color = x.p.color  # Set sibling's color to parent's color
                    x.p.color = 0  # Set parent's color to black
                    s.right.color = 0  # Set right child of sibling to black
                    self.LR(x.p)  # Call left rotation on parent
                    x = self.root  # Set x to root (tree is balanced)
            else:  # If x is right child of its parent
                s = x.p.left  # Sibling of x
                if s.color == 1:  # If sibling is red
                    s.color = 0  # Set sibling's color to black
                    x.p.color = 1  # Make parent's color red
                    self.RR(x.p)  # Call right rotation on parent
                    s = x.p.left  # Update sibling
                if s.right.color == 0 and s.left.color == 0:  # If both children of sibling are black
                    s.color = 1  # Set sibling's color to red
                    x = x.p  # Move x up to parent
                else:
                    if s.left.color == 0:  # If left child of sibling is black
                        s.right.color = 0  # Set right child of sibling to black
                        s.color = 1  # Set sibling's color to red
                        self.LR(s)  # Call left rotation on sibling
                        s = x.p.left  # Update sibling after rotation

                    s.color = x.p.color  # Set sibling's color to parent's color
                    x.p.color = 0  # Set parent's color to black
                    s.left.color = 0  # Set left child of sibling to black
                    self.RR(x.p)  # Call right rotation on parent
                    x = self.root  # Set x to root (tree is balanced)
        x.color = 0  # Ensure x is black



    # Function to transplant nodes
    def __rb_transplant ( self , u , v ) :
        if u.p == None :
            self.root = v
        elif u == u.p.left :
            u.p.left = v
        else :
            u.p.right = v
        v.p = u.p

    # Function to return node containing the given key
    def Tree_Search( self, k):
        x = self.root
        while x != self.NULL and k != x.key:
            if k < x.key:
                x = x.left
            else:
                x = x.right
        return x

    # Function to return succesor of x
    def Tree_Successor(self, x):
        if x.right != self.NULL:
            return self.Tree_Minimum(x.right)
        y = x.p
        while y != self.NULL and x == y.right:
            x = y
            y = y.p
        return y

    # Function to return succesor of x
    def Tree_Predecessor(self, x):
        if x.left != self.NULL:
            return self.Tree_Maximum(x.left)
        y = x.p
        while y != self.NULL and x == y.left:
            x = y
            y = y.p
        return y

    # Function to handle deletion
    def delete_node_helper ( self , node , key ) :
        z = self.NULL
        while node != self.NULL :                          # Search for the node having that value/ key and store it in 'z'
            if node.key == key :
                z = node

            if node.key <= key :
                node = node.right
            else :
                node = node.left

        if z == self.NULL :                                # If Kwy is not present then deletion not possible so return
            print ( "Value not present in Tree !!" )
            return
        else:
            self.RB_Delete(z)

    def RB_Delete(self, z):
        y = z
        y_original_color = y.color

        if z.left == self.NULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif z.right == self.NULL:
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.Tree_Minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.p == z:
                x.p = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.p = y
            y.color = z.color

        if y_original_color == 0:
            self.fixDelete(x)


    # Deletion of node
    def delete ( self , key ) :
        self.delete_node_helper ( self.root , key )         # Call for deletion


    # Function to print
    def __printCall ( self , node , indent , last ) :
        if node != self.NULL :
            print(indent, end=' ')
            if last :
                print ("R----",end= ' ')
                indent += "     "
            else :
                print("L----",end=' ')
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print ( str ( node.key ) + "(" + s_color + ")" )
            self.__printCall ( node.left , indent , False )
            self.__printCall ( node.right , indent , True )

    # Function to call print
    def print_RBTree ( self ) :
        self.__printCall ( self.root , "" , True )



rbt = RBTree()
items = [5,10,15,20,25,30,35,40,45,50,55]
for i in items:
    rbt.RB_Insert(RB_Node(i))
    rbt.print_RBTree()
    print()


rbt.RB_Delete(RB_Node(25))
rbt.print_RBTree()
print()
rbt.RB_Delete(RB_Node(40))
rbt.print_RBTree()
print()
rbt.RB_Insert(RB_Node(-10))
rbt.print_RBTree()
print()

# rbtroot = RBTree()
# N = [1000,2000,4000,8000]
# for n in N:
#     for i in range(n):
#         rbtroot.insert(i)
#     counter = 0 
#     k = 2*n     # n is the number of keys inserted 
#     for i in range(n): 
#         v = random.randint(0, k) 
#         x = rbtroot.Tree_Search(v)    # rbt is the Red-Black Tree 
#         if x != rbtroot.NULL: 
#             counter += 1 
#     print(f"N:{n}, counter:{counter}")

# rbtroot.print_RBTree()
