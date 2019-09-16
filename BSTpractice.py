class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        i_node = self.root

        while True:
            if new_val > i_node.value:
                if not i_node.right:
                    i_node.right = Node(new_val)
                    return
                i_node = i_node.right
            elif new_val < i_node.value:
                if not i_node.left:
                    i_node.left = Node(new_val)
                    return
                i_node = i_node.left
        pass

    def search(self, find_val):
        s_node = self.root

        while True:
            if s_node:
                if find_val == s_node.value:
                    return True
                elif find_val > s_node.value:
                    s_node = s_node.right
                elif find_val < s_node.value:
                    s_node = s_node.left
            return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return str(self.root.value) + self.preorder_print(self.root.left) + self.preorder_print(self.root.right)

    def preorder_print(self, start):
        """Helper method - use this to create a 
        recursive print solution."""
        if not start:
            return ""
        return "-" + str(start.value) + self.preorder_print(start.left) + self.preorder_print(start.right)

    
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))
print(tree.print_tree())