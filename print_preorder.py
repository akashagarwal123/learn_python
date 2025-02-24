def printpreorder(root):
    if root:
        print(root.data,end=' ')
        printpreorder(root.left)
        printpreorder(root.right)