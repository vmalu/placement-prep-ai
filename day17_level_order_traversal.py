# Day 17 - Level Order Traversal (Python 3)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: TreeNode) -> list[int]:
    if not root:
        return []
        
    result = []
    queue = [root]
    
    while queue:
        current = queue.pop(0)  # Dequeue front node
        result.append(current.val)
        
        # Enqueue left and right children
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
            
    return result

# Test Tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

print("Python BFS Result:", level_order_traversal(root))
# Expected Output: [1, 2, 3, 4, 5, 6]
