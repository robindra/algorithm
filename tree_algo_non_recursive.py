class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the BST iteratively."""
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    def search(self, value):
        """Searches for a value in the BST iteratively."""
        current = self.root
        while current:
            if value == current.value:
                return True
            elif value < current.value:
                current = current.left
            else:
                current = current.right
        return False

    def delete(self, value):
        """Deletes a value from the BST iteratively."""
        parent = None
        current = self.root

        # Find the node to delete and its parent
        while current and current.value != value:
            parent = current
            if value < current.value:
                current = current.left
            else:
                current = current.right

        # If node to delete was not found, return
        if current is None:
            return

        # Case 1: Node has no children
        if current.left is None and current.right is None:
            if current != self.root:
                if parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
            else:
                self.root = None

        # Case 2: Node has two children
        elif current.left and current.right:
            successor = self.get_min_node(current.right)
            val = successor.value
            self.delete(successor.value)
            current.value = val

        # Case 3: Node has one child
        else:
            child = current.left if current.left else current.right
            if current != self.root:
                if current == parent.left:
                    parent.left = child
                else:
                    parent.right = child
            else:
                self.root = child

    def get_min_node(self, node):
        """Finds the minimum value node starting from a given node."""
        while node.left:
            node = node.left
        return node

    def in_order_traversal(self):
        """In-order traversal of the BST using an iterative approach."""
        stack = []
        current = self.root

        while stack or current:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.value, end=" ")
            current = current.right


# Example usage of the BinarySearchTree class
bst = BinarySearchTree()

# Insert elements into the BST
for value in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(value)

print("In-order Traversal:")
bst.in_order_traversal()  # Expected output: 3 5 7 10 12 15 18

# Search for a value in the BST
value_to_search = 7
found = bst.search(value_to_search)
print(f"\n\nSearch for {value_to_search}: {'Found' if found else 'Not Found'}")

# Delete a node from the BST
bst.delete(10)
print("\nIn-order Traversal after deleting 10:")
bst.in_order_traversal()  # Expected output: 3 5 7 12 15 18
