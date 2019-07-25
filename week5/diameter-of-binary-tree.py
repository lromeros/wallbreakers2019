# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTreeHelper(self, root: TreeNode, max_distance) -> int:
        if root is None:
            return (0, max_distance)
        
        left_depth, left_max_dist = self.diameterOfBinaryTreeHelper(root.left, max_distance)
        right_depth, right_max_dist = self.diameterOfBinaryTreeHelper(root.right, max_distance)
        
        max_depth = 1 + max(left_depth, right_depth)
        max_distance = max(max_distance, left_max_dist, right_max_dist, left_depth + right_depth)

        return (max_depth, max_distance)

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if root is None or (root.left is None and root.right is None):
            return 0
        return self.diameterOfBinaryTreeHelper(root, 0)[1]

