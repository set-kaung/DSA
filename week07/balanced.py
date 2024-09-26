from BinarySearchTree import *
 
def balancedInsert(root:BSTree,arr,start,end):
    if start <= end:
        mid = (end+start)//2
        root.Tree_Insert(BST_Node(arr[mid]))
        balancedInsert(root,arr,start,mid-1)
        balancedInsert(root,arr,mid+1,end)
        

balanced = BSTree()

arr = [3,11,16,22,24,30,38,40,51,60,63,65,67,70,95]

balancedInsert(balanced,arr,0,len(arr)-1)
balanced.print_BSTree()

# unbalanced = BSTree()
# for i in arr:
#     unbalanced.Tree_Insert(BST_Node(i))

# unbalanced.print_BSTree()

print(balanced.Tree_Predecessor(balanced.Tree_Search(51)).key)