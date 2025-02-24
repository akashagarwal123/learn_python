class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def buildtree(root,data):
    if root is None:
        root = Node(data)
    if root is not None:
        if data < root.data:
            if root.left is None:
                root.left = Node(data)
            else:
                buildtree(root.left,data)
        else:
            if root.right is None:
                root.right = Node(data)
            else:
                buildtree(root.right,data)
def inorder(root):
    if root:
        print(root.data,end=' ')
        inorder(root.left)
        inorder(root.right)
    
def diagonal(root,q):
    if root is None:
        return
    if root:
        print(root.data,end=' ')
    if root.left is not None:
        q.append(root.left)
    if root is not None:
        diagonal(root.right,q)
    if root.right is None:
        while(len(q)!=0):
            temp = q.pop(0)
            diagonal(temp,q)
    

        
            
lst = [8,20,9,15,25,5,2,7,14,18,1,3,6,4]
root = Node(10)
for i in lst:
    buildtree(root,i)
print('The inorder of the tree is: ')
inorder(root)
print('\n')
q=[]
print('The diagonal traversal of the tree is: ')
diagonal(root,q)