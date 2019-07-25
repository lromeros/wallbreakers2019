# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def get_leaves(self, root: TreeNode) -> List[int]:
        queue = [root]
        leaf_values = []
        
        while len(queue) > 0:
            root = queue.pop()
            if root.left == None and root.right == None:
                leaf_values.append(root.val)
            if root.left is not None:
                queue.append(root.left)
            if root.right is not None:
                queue.append(root.right)
        
        return leaf_values
        
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        root1_leaves = self.get_leaves(root1) if root1 is not None else []
        root2_leaves = self.get_leaves(root2) if root2 is not None else []
        
        return root1_leaves == root2_leaves
