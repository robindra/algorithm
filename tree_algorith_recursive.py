class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Inserts a value into the BST."""
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if node is None:
            return TreeNode(value)
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        else:
            node.right = self._insert_recursive(node.right, value)
        return node

    def delete(self, value):
        """Deletes a value from the BST."""
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            # Node with two children
            temp_val = self._min_value(node.right)
            node.value = temp_val
            node.right = self._delete_recursive(node.right, temp_val)
        return node

    def search(self, value):
        """Searches for a value in the BST."""
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    def in_order_traversal(self):
        """In-order traversal of the BST."""
        self._in_order_recursive(self.root)

    def _in_order_recursive(self, node):
        if node:
            self._in_order_recursive(node.left)
            print(node.value, end=" ")
            self._in_order_recursive(node.right)

    def pre_order_traversal(self):
        """Pre-order traversal of the BST."""
        self._pre_order_recursive(self.root)

    def _pre_order_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self._pre_order_recursive(node.left)
            self._pre_order_recursive(node.right)

    def post_order_traversal(self):
        """Post-order traversal of the BST."""
        self._post_order_recursive(self.root)

    def _post_order_recursive(self, node):
        if node:
            self._post_order_recursive(node.left)
            self._post_order_recursive(node.right)
            print(node.value, end=" ")

    def min_value(self):
        """Finds the minimum value in the BST."""
        return self._min_value(self.root)

    def _min_value(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current.value if current else None

    def max_value(self):
        """Finds the maximum value in the BST."""
        return self._max_value(self.root)

    def _max_value(self, node):
        current = node
        while current and current.right:
            current = current.right
        return current.value if current else None


# Example usage of the BinarySearchTree class
bst = BinarySearchTree()

# Insert elements into the BST
for value in [10, 5, 15, 3, 7, 12, 18]:
    bst.insert(value)

print("In-order Traversal:")
bst.in_order_traversal()  # Expected output: 3 5 7 10 12 15 18
print("\nPre-order Traversal:")
bst.pre_order_traversal()  # Expected output: 10 5 3 7 15 12 18
print("\nPost-order Traversal:")
bst.post_order_traversal()  # Expected output: 3 7 5 12 18 15 10

# Search for a value in the BST
value_to_search = 7
found = bst.search(value_to_search)
print(f"\n\nSearch for {value_to_search}: {'Found' if found else 'Not Found'}")

# Delete a node from the BST
bst.delete(10)
print("\nIn-order Traversal after deleting 10:")
bst.in_order_traversal()  # Expected output: 3 5 7 12 15 18

# Find minimum and maximum values in the BST
print("\n\nMinimum value in the BST:", bst.min_value())  # Expected output: 3
print("Maximum value in the BST:", bst.max_value())  # Expected output: 18
