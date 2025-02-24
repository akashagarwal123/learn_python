leaf=[]
left=[]
right=[]
# print the leaf nodes
def printleafnodes(root):
    if root:
        if root.left is None and root.right is None:
            leaf.append(root.data)
        printleafnodes(root.left)
        printleafnodes(root.right)
#print the left nodes of the tree
def printleftnodes(root):
    if root:
        if root.left is not None:
            left.append(root.data)
        printleftnodes(root.left)
# print the right nodes of the tree
def printrightnodes(root):
    if root:
        if root.right is not None or root.left is not None:
            right.append(root.data)
        printrightnodes(root.right)
def boundary_traversal(root):
    printleftnodes(root)
    printleafnodes(root)
    printrightnodes(root)
    print(*left,end=' ')
    print(*leaf,end=' ')
    print(*right[:0:-1],end=' ')
