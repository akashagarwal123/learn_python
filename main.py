import create_node_of_a_tree as treenode
from buildtree import buildtree
from print_preorder import printpreorder
from print_inorder import inorder
from print_postorder import postorder
from print_levelorder import printlevelorder
from insert_new_element import insert
from inser_new_element_using_queue import insertusingqueue
from print_level_order_spiral_form import print_levelorder_spiral
from delete_element import delete_element
from sum_tree import sum_tree
from boundary_traversal import boundary_traversal
def main():
    lst=[11,7,9,15,8]
    root = treenode.Node(10)
    for i in lst:
        buildtree(root,i)
    print('The original preorder is: ')
    printpreorder(root)
    print('\n')
    print('The original inorder is: ')
    inorder(root)
    print('\n')
    print('The original postorder is: ')
    postorder(root)
    print('\n')
    print('The original Level order of the tree is: ')
    printlevelorder(root)
    insert(root,100)
    insert(root,0)
    print('\n')
    print('The preorder after insertion of 0 and 100 is: ')
    printpreorder(root)
    print('\n')
    print('The inorder after insertion of 0 and 100 is: ')
    inorder(root)
    print('\n')
    print('The postorder after insertion of 0 and 100 is: ')
    postorder(root)
    print('\n')
    print('The Level Order of the tree after insertion of 18 and 20')
    printlevelorder(root)
    insertusingqueue(root,18)
    insertusingqueue(root,20)
    print('\n')
    print('The inorder after insertion of 18 is: ')
    inorder(root)
    print('\n')
    print('The Level order traveral of the given tree is: ')
    printlevelorder(root)
    print('\n')
    print('The Level order traveral of the given tree in spiral form is: ')
    print_levelorder_spiral(root)
    '''print('\n')
    print('Delete 15 and 10 from given tree: ')
    #delete_element(root,15)
    delete_element(root,10)
    print('\n')
    print('The Level order traveral of the given tree in spiral form is: ')
    print_levelorder_spiral(root)'''
    print('\n')
    print('The given tree is a sumtree or not a sum tree:')
    sum_tree(root)
    print('\n')
    print('The boundary traversal of the given tree is: ')
    boundary_traversal(root)
main()