# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longest_univalues(self, root: TreeNode):
        # represents the length of the greatest valid subpath (connects two children) contained at this node, 
        # doesn't necessarily have to include this node
        max_subpath = 0
        # represents the length of the greatest valid path that contains this node
        max_continuing = 0
        
        if root is not None and not (root.left is None and root.right is None):
            left_subpath, left_continuing = self.longest_univalues(root.left)
            right_subpath, right_continuing = self.longest_univalues(root.right)
            
            continues_left = root.left is not None and root.val == root.left.val
            continues_right = root.right is not None and root.val == root.right.val
            
            max_subpath = max(left_subpath, left_continuing, right_subpath, right_continuing)
            
            if continues_left and continues_right:
                # both children are the same value as the root
                max_subpath = max(max_subpath, left_continuing + right_continuing + 2)
                max_continuing = 1 + max(left_continuing, right_continuing)
            elif continues_left:
                # only the left child is the same value
                max_continuing = 1 + left_continuing
            elif continues_right:
                # only the right child is the same value
                max_continuing = 1 + right_continuing
            
        return (max_subpath, max_continuing)
        
    def longestUnivaluePath(self, root: TreeNode) -> int:
        return max(self.longest_univalues(root))
        
