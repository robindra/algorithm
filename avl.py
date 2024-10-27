class AVLNode:
    """A node in the AVL Tree."""
    def __init__(self, key):
        self.left = None  # Left child
        self.right = None  # Right child
        self.val = key  # Node value
        self.height = 1  # Height of the node (new nodes are initially added as leaves)

class AVLTree:
    """AVL Tree implementation."""
    
    def insert(self, root, key):
        """Inserts a new key into the AVL Tree and balances the tree.
        
        Args:
            root: The root node of the AVL tree.
            key: The value to be inserted.
        
        Returns:
            The root of the modified AVL Tree.
        """
        # Step 1 - Perform normal BST insert
        if not root:
            return AVLNode(key)  # Create a new node if tree is empty
        elif key < root.val:
            root.left = self.insert(root.left, key)  # Insert in the left subtree
        else:
            root.right = self.insert(root.right, key)  # Insert in the right subtree

        # Step 2 - Update the height of the ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor of this ancestor node
        balance = self.getBalance(root)

        # If this node becomes unbalanced, then there are 4 cases

        # Left Left Case
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)  # Right rotation to balance

        # Right Right Case
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)  # Left rotation to balance

        # Left Right Case
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)  # Left rotation on left child
            return self.rightRotate(root)  # Right rotation to balance

        # Right Left Case
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)  # Right rotation on right child
            return self.leftRotate(root)  # Left rotation to balance

        return root

    def leftRotate(self, z):
        """Performs a left rotation on the subtree rooted at z.
        
        Args:
            z: The root of the subtree to be rotated.
        
        Returns:
            The new root of the rotated subtree.
        """
        y = z.right  # Set y
        T2 = y.left  # Store T2
        # Perform rotation
        y.left = z
        z.right = T2
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        """Performs a right rotation on the subtree rooted at z.
        
        Args:
            z: The root of the subtree to be rotated.
        
        Returns:
            The new root of the rotated subtree.
        """
        y = z.left  # Set y
        T3 = y.right  # Store T3
        # Perform rotation
        y.right = z
        z.left = T3
        # Update heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def getHeight(self, root):
        """Returns the height of the node.
        
        Args:
            root: The node whose height is to be determined.
        
        Returns:
            The height of the node, or 0 if the node is None.
        """
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        """Calculates the balance factor of the node.
        
        Args:
            root: The node whose balance factor is to be calculated.
        
        Returns:
            The balance factor of the node.
        """
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def inorder(self, root):
        """Returns the inorder traversal of the AVL Tree.
        
        Args:
            root: The root node of the AVL tree.
        
        Returns:
            A list of node values in sorted order.
        """
        # Inorder traversal: left, root, right
        return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

# Example usage
avl = AVLTree()
root_avl = None
values_avl = [30, 20, 40, 10, 25]  # Sample values to insert into the AVL Tree
for value in values_avl:
    root_avl = avl.insert(root_avl, value)  # Insert each value into the AVL Tree

# Print the inorder traversal of the AVL Tree
print("Inorder Traversal of AVL Tree:", avl.inorder(root_avl))
