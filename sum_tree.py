def sum_tree(root):
    sum_observed = root
    q=[]
    q.append(root)
    sum_calaculated = 0
    while(len(q)!=0):
        temp = q.pop(0)
        sum_calaculated+=temp.data
        if temp.left is not None:
            q.append(temp.left)
        if temp.right is not None:
            q.append(temp.right)
    if(sum_observed==sum_calaculated):
        print("Is a sum tree")
    else:
        print("Is not a sumtree")


