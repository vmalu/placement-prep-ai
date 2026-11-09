# Day 19 - Diameter of a Binary Tree (Python 3)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    max_diameter = 0
    
    def get_height(node: TreeNode) -> int:
        nonlocal max_diameter
        if node is None:
            return 0
            
        left_height = get_height(node.left)
        right_height = get_height(node.right)
        
        # Longest path through this node in terms of edges
        max_diameter = max(max_diameter, left_height + right_height)
        
        # Return height of this node
        return 1 + max(left_height, right_height)
        
    get_height(root)
    return max_diameter

# Test Tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3)

print("Python Diameter (Edges):", diameter_of_binary_tree(root))
# Expected Output: 3 (Path: 4 -> 2 -> 1 -> 3 or 5 -> 2 -> 1 -> 3)
