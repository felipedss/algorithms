# A class that represents an individual node in a
# Binary Tree
class Node:

    def __init__(self, value):
        self.left = None
        self.right = None
        self.val = value

# left -> right -> root
class PostOrderTraversal:

    def print_post_order(self, tree):

        if tree is None:
            return

        self.print_post_order(tree.left)

        self.print_post_order(tree.right)

        print(tree.val, end=" ")
        
    
postOrderTraversal = PostOrderTraversal()        

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

postOrderTraversal.print_post_order(root)  # 4 5 2 3 1