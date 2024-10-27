class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sorted_array_to_bst(nums):
    if not nums:
        return None

    mid = len(nums) // 2  # Find the middle index
    root = TreeNode(nums[mid])  # Create a node with the middle element

    # Recursively build the left and right subtrees
    root.left = sorted_array_to_bst(nums[:mid])  # Left half
    root.right = sorted_array_to_bst(nums[mid + 1:])  # Right half

    return root

def print_tree(root):
    """Helper function to print the tree in level order for easier visualization."""
    if not root:
        return "[]"

    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result

# Example usage:
nums = [-10, -3, 0, 5, 9]
bst_root = sorted_array_to_bst(nums)
bst_output = print_tree(bst_root)

print("Output:", bst_output)  # Output: [0, -10, 5, None, -3, None, 9]
