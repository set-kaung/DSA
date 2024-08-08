# Name: Set Kaung Lwin
# ID: 6632017
# Sec: 543

import random
import time
# ---- BS Tree -----


from BinarySearchTree import *

'''
bst = BSTree()
a = [4, 5, 12, -5, -87, 9, 1023]

import random

random.shuffle(a)

for k in a:
    x = BST_Node(k)
    bst.Tree_Insert(x)
    
bst.print_BSTree()
'''

# bst2 = BSTree()
# for k in [56,70,30,60,65,22,11,16,40,95,63,3,67]:
#     x = BST_Node(k)
#     bst2.Tree_Insert(x)

# bst2.print_BSTree()
# x = bst2.Tree_Search(40)
# bst2.Tree_Delete(x)
# bst2.print_BSTree()

print("Binary Search Tree")
bstroot = BSTree()
N = [1000, 2000, 4000, 8000]
for n in N:
    st = time.process_time()
    for i in range(n):
        bstroot.Tree_Insert(BST_Node(i))
    counter = 0
    k = 2 * n
    for i in range(n):
        v = random.randint(0, k)
        # print(v)
        x = bstroot.Tree_Search(v)
        if x != None:
            counter += 1
    et = time.process_time()
    print(f"N:{n}, counter:{counter}, time:{et - st}")

# ---- RB Tree -----

from RedBlackTree import *

# rbt = RBTree()
# a = [12,5,3,11,15,7,10,13,14,6,4,17,8]
# for k in a:
#     rbt.insert(k)
# rbt.print_RBTree()

# rbt.delete(5)
# rbt.print_RBTree()


print("Red Black Tree")
rbtroot = RBTree()
N = [1000, 2000, 4000, 8000]
for n in N:
    st = time.process_time()
    for i in range(n):
        rbtroot.RB_Insert(BST_Node(i))
    counter = 0
    k = 2 * n
    for i in range(n):
        v = random.randint(0, k)
        # print(v)
        x = rbtroot.Tree_Search(v)
        if x != rbtroot.NULL:
            counter += 1
    et = time.process_time()
    print(f"N:{n}, counter:{counter}, time:{et - st}")
