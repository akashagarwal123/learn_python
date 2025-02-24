def print_levelorder_spiral(root):
    if root is None:
        return
    s1=[]
    s2=[]
    s1.append(root)
    while(len(s1)!=0 or len(s2)!=0):
        while(len(s1)!=0):
            temp=s1.pop()
            print(temp.data,end=' ')
            if temp.right:
                s2.append(temp.right)
            if temp.left:
                s2.append(temp.left)
        while(len(s2)!=0):
            temp=s2.pop()
            print(temp.data,end=' ')
            if temp.left:
                s1.append(temp.left)
            if temp.right:
                s1.append(temp.right)
