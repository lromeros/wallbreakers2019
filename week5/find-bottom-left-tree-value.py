# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def find_bottom_left(self, root: TreeNode, max_depth: int): #returns (max_depth: int, left_most_val: int)
        has_left = root.left is not None
        has_right = root.right is not None
        bottom_left = root.val 
        
        if has_left:
            left_depth, left_left = self.find_bottom_left(root.left, 1 + max_depth)
        if has_right:
            right_depth, right_left = self.find_bottom_left(root.right, 1 + max_depth)
            
        if has_left and has_right:
            bottom_left = left_left if left_depth >= right_depth else right_left
            max_depth = max(left_depth, right_depth)
        elif has_left and not has_right:
            max_depth = left_depth
            bottom_left = left_left
        elif not has_left and has_right:
            max_depth = right_depth
            bottom_left = right_left

        return (max_depth, bottom_left)
    
    
    def findBottomLeftValue(self, root: TreeNode) -> int:
        return self.find_bottom_left(root, 0)[1]
