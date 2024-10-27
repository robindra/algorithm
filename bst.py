class Node:
    """A node in the Binary Search Tree."""
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.val = key  # Node value

class BST:
    """Binary Search Tree implementation."""
    
    def insert(self, root, key):
        """Inserts a new key into the BST.
        
        Args:
            root: The root node of the BST.
            key: The value to be inserted.
        
        Returns:
            The root of the modified BST.
        """
        # If the tree is empty, create a new node and return it
        if root is None:
            return Node(key)
        else:
            # Recur down the tree to find the correct position to insert the new node
            if key < root.val:
                root.left = self.insert(root.left, key)  # Insert in the left subtree
            else:
                root.right = self.insert(root.right, key)  # Insert in the right subtree
        return root

    def search(self, root, key):
        """Searches for a key in the BST.
        
        Args:
            root: The root node of the BST.
            key: The value to be searched.
        
        Returns:
            The node containing the key if found, otherwise None.
        """
        # Base Cases: root is null or key is present at root
        if root is None or root.val == key:
            return root
        # Key is greater than root's key, search in the right subtree
        if key > root.val:
            return self.search(root.right, key)
        # Key is smaller than root's key, search in the left subtree
        return self.search(root.left, key)

    def inorder(self, root):
        """Returns the inorder traversal of the BST.
        
        Args:
            root: The root node of the BST.
        
        Returns:
            A list of node values in sorted order.
        """
        # Inorder traversal: left, root, right
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

# Example usage
bst = BST()
root = None
values = [30, 20, 40, 10, 25]  # Sample values to insert into the BST
for value in values:
    root = bst.insert(root, value)  # Insert each value into the BST

# Print the inorder traversal of the BST
print("Inorder Traversal of BST:", bst.inorder(root))
# Search for a value (25) in the BST
print("Searching for 25:", bst.search(root, 25) is not None)
