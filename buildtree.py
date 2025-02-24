import create_node_of_a_tree as treenode
def buildtree(root,data):
    if data < root.data:
        if root.left is None:
            root.left = treenode.Node(data)
        else:
            buildtree(root.left,data)
    else:
        if root.right is None:
            root.right = treenode.Node(data)
        else:
            buildtree(root.right,data)