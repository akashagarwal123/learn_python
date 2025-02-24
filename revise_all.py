count=0

'''
The below logic is used to initialize an empty 
node to the tree
'''
class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None
'''
The below build_tree function is used to 
add elements or nodes to the tree
''' 
def build_tree(root,data):
    if root:
        if data<=root.data:
            if root.left is None:
             root.left = Node(data)
            else:
             build_tree(root.left,data)
        if data>root.data:
            if root.right is None:
             root.right = Node(data)
            else:
             build_tree(root.right,data)
'''
The below function is used to 
print the inorder traversal of 
a binary tree
'''
def print_tree_inorder(root):
    if root:
        print_tree_inorder(root.left)
        print(root.data,end=" ")
        print_tree_inorder(root.right)
'''
The below function is used to print 
the post order tree traversal of the 
binary tree.
'''
def print_tree_postorder(root):
   if root:
      print_tree_postorder(root.right)
      print(root.data,end=" ")
      print_tree_postorder(root.left)
'''
The below function is used to print the 
pre order traversal of the given binary tree
'''
def print_tree_preorder(root):
   if root:
      print(root.data,end=" ")
      print_tree_preorder(root.left)
      print_tree_preorder(root.right)
'''
The below function is used to 
insert a new element into the 

'''   
def insert_new_node(root,data):
   if root:
      if data<root.data:
         if root.left is None:
            root.left = Node(data)
         else:
            insert_new_node(root.left,data)
      if data>=root.data:
          if root.right is None:
             root.right = Node(data)
          else:
             insert_new_node(root.right,data)
'''
The below function is used to search an element 
within a tree.
'''
def search_element(root,data):
 if root:
   if root.data == data:
      print("The seach for the element is successful",root.data)
   else:
         if data <= root.data:
            search_element(root.left,data)
         else:
            search_element(root.right,data)
 else:
    print("The search is unsuccessful")

'''
'''           
def element_occurrence(root,data,count):
   if root:
      if root.data==data:
         count=count+1
      element_occurrence(root.left,data,count)
      element_occurrence(root.right,data,count)
   return(count)

def main():
    l=[] # inputting a blank list
    
    n = int(input("Enter the number of nodes to be entered to the list: "))
    
    '''
    Entering the value of the nodes for the tree
    '''
    for i in range(0,n):
       x = int(input("Enter the node: "))
       l.append(x)

    r = int(input("Enter the root value: "))
    root = Node(r)

    '''
    Calling the build tree function to create a tree 
    '''
    for i in l:
        build_tree(root,i)

    print("The inoder traversal of the tree is :")
    print_tree_inorder(root)

    print("\n")

    print("The postoder traversal of the tree is: ")
    print_tree_postorder(root)

    print("\n")

    print("The preoder traversal of the tree is: ")
    print_tree_preorder(root)

    print("\n")

    y = int(input("Enter the number to be searched: "))
    search_element(root,y)

    data = int(input("Enter the number to be counted: "))
    store = element_occurrence(root,data,count)
    print(store)
main()

        