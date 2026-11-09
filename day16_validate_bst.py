# Day 16 - Validate Binary Search Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    def validate(node: TreeNode, low: float, high: float) -> bool:
        # An empty subtree is a valid BST
        if node is None:
            return True
            
        # Current node value must be strictly within bounds
        if not (low < node.val < high):
            return False
            
        # Left child must be < node.val; Right child must be > node.val
        return (validate(node.left, low, node.val) and 
                validate(node.right, node.val, high))
                
    return validate(root, float('-inf'), float('inf'))

# Test Case 1: Valid BST
#       2
#      / \
#     1   3
valid_root = TreeNode(2, TreeNode(1), TreeNode(3))
print("Test 1 (Valid BST):", is_valid_bst(valid_root))  # Expected: True

# Test Case 2: Invalid BST (Node 3 is in right subtree of 5, but 3 < 5)
#       5
#      / \
#     1   6
#        / \
#       3   7
invalid_root = TreeNode(5, TreeNode(1), TreeNode(6, TreeNode(3), TreeNode(7)))
print("Test 2 (Invalid BST):", is_valid_bst(invalid_root))  # Expected: False
