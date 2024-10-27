class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, root, key):
        if key < root.value:
            if root.left is None:
                root.left = Node(key)
            else:
                self._insert_rec(root.left, key)
        else:
            if root.right is None:
                root.right = Node(key)
            else:
                self._insert_rec(root.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, root, key):
        if root is None or root.value == key:
            return root
        if key < root.value:
            return self._search_rec(root.left, key)
        return self._search_rec(root.right, key)

    def inorder(self):
        return self._inorder_rec(self.root)

    def _inorder_rec(self, root):
        return self._inorder_rec(root.left) + [root.value] + self._inorder_rec(root.right) if root else []

# Driver code
if __name__ == "__main__":
    bst = BST()
    values = [10, 5, 20, 3, 7, 15, 30]
    for value in values:
        bst.insert(value)

    print("In-order traversal of the BST:", bst.inorder())

    # Searching for a value
    search_value = 15
    result = bst.search(search_value)
    if result:
        print(f"Value {search_value} found in the BST.")
    else:
        print(f"Value {search_value} not found in the BST.")
