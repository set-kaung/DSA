import math

class Node:
    def __init__(self, data:int) -> None:
        self.data = data
        self.Left:Node|None = None
        self.Right:Node|None = None


def showHelper(root:Node|None,depth) -> None:
        if root is not None:
            print()
            print(f"{"  "*depth}{root.data}",end="  ")
            showHelper(root.Left, depth-1)
            showHelper(root.Right, depth+1)

def insertHelper(root,node) -> Node:
        if root is None:
            root = node
            return root
        else:
            if node.data < root.data:
                root.Left = insertHelper(root.Left,node)
            else:
                
                root.Right = insertHelper(root.Right, node)

        return root

class BinarySearchTree:
    def __init__(self) -> None:
        self.Root = None
        self.depth = 0
        self.count = 0
        pass

    
    
    def insert(self, node:Node) ->None:
        self.count += 1
        self.depth = math.floor(math.log(self.count,2))
        self.Root = insertHelper(self.Root,node)
        
    def show(self) -> None:
        showHelper(self.Root,self.depth+1)
        print()

    

n = BinarySearchTree()
n.insert(Node(10))
n.insert(Node(12))
n.insert(Node(9))
n.insert(Node(8))
n.insert(Node(15))
n.insert(Node(3))
n.insert(Node(90))
n.insert(Node(2))


n.show()
# print(n.depth)