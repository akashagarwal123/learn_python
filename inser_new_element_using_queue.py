import create_node_of_a_tree as treenode
def insertusingqueue(root,data):
    if root is None:
        root = treenode.Node(data)
    q=[]
    q.append(root)
    while(len(q)):
        temp = q[0]
        q.pop(0)
        if data<temp.data:
            if temp.left is None:
                temp.left = treenode.Node(data)
            else:
                q.append(temp.left)
        else:
            if temp.right is None:
                temp.right = treenode.Node(data)
            else:
                q.append(temp.right)