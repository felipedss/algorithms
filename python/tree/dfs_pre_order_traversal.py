# A class that represents an individual node in a
# Binary Tree
class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# root -> left -> right
class PreOrderTraversal:

    def print_pre_order(self, tree):

        if tree == None:
            return

        # Then print the data of node
        print(tree.val, end=" ")            
        
        self.print_pre_order(tree.left)

        self.print_pre_order(tree.right)


preOrderTraversal = PreOrderTraversal()        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

preOrderTraversal.print_pre_order(root)  # 1 2 4 5 3