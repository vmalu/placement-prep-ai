# Day 15 - Invert a Binary Tree

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    if root is None:
        return None
        
    # Recursively swap left and right subtrees
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    
    return root

# Helper function to print Level Order (BFS) traversal
def level_order(root: TreeNode) -> list[int]:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

# Test tree:
#       4
#     /   \
#    2     7
#   / \   / \
#  1   3 6   9
root = TreeNode(4)
root.left = TreeNode(2, TreeNode(1), TreeNode(3))
root.right = TreeNode(7, TreeNode(6), TreeNode(9))

print("Original Tree (Level Order):", level_order(root))
inverted_root = invert_tree(root)
print("Inverted Tree (Level Order):", level_order(inverted_root))
# Expected Inverted: [4, 7, 2, 9, 6, 3, 1]
