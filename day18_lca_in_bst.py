# Day 18 - Lowest Common Ancestor in BST (Python 3)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: int, q: int) -> int:
    curr = root
    
    while curr:
        # If both values are smaller, LCA is in the left subtree
        if p < curr.val and q < curr.val:
            curr = curr.left
        # If both values are larger, LCA is in the right subtree
        elif p > curr.val and q > curr.val:
            curr = curr.right
        # Split point found: this node is the LCA
        else:
            return curr.val
            
    return -1

# Test BST:
#         6
#       /   \
#      2     8
#     / \   / \
#    0   4 7   9
#       / \
#      3   5
root = TreeNode(6)
root.left = TreeNode(2, TreeNode(0), TreeNode(4, TreeNode(3), TreeNode(5)))
root.right = TreeNode(8, TreeNode(7), TreeNode(9))

print("Python LCA of (2, 8):", lowest_common_ancestor(root, 2, 8))  # Expected: 6
print("Python LCA of (2, 4):", lowest_common_ancestor(root, 2, 4))  # Expected: 2
print("Python LCA of (3, 5):", lowest_common_ancestor(root, 3, 5))  # Expected: 4
