def delete_element(root,data):
    if root is None:
        return
    q=[]
    keynode = None
    temp = None
    last = None
    q.append(root)
    while(len(q)!=0):
        temp = q.pop(0)
        if temp.data == data:
            keynode = temp
        if temp.left is not None:
            last = temp
            q.append(temp.left)
        if temp.right is not None:
            last = temp
            q.append(temp.right)
    if keynode is not None:
        keynode.data = temp.data
        temp.data =-1

