# A class that represents an individual node in a
# Binary Tree
class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# left -> root -> right
class InOrderTraversal:

    def print_in_order(self, tree):

        if tree == None:
            return
        
        # First recur on left child
        self.print_in_order(tree.left)
        
        # Then print the data of node
        print(tree.val, end=" ")

        # Now recur on right child
        self.print_in_order(tree.right)


inOrderTraversal = InOrderTraversal()        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

inOrderTraversal.print_in_order(root)  # 4 2 5 1 3