def printlevelorder(root):
    if root is None:
        return
    q=[]
    q.append(root)
    while(len(q)):
        temp = q[0]
        print(temp.data,end=' ')
        q.pop(0)
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)