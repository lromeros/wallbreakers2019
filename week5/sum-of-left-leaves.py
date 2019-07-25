# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def is_leaf(self, node: TreeNode) -> bool:
        return node is not None and node.left is None and node.right is None
    
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        _sum = 0
        stack = [root] if root is not None else []
        
        while len(stack) > 0:
            root = stack.pop()
            
            if root.left is not None:
                _sum += root.left.val if self.is_leaf(root.left) else 0
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
        
        return _sum
