# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def add_child_to_lists(self, p_child, p_list, q_child, q_list):
        if p_child is not None and q_child is not None:
            p_list.append(p_child)
            q_list.append(q_child)
            return True
        elif p_child is None and q_child is None:
            return True
        else:
            return False
        
        
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is not None or q is None and p is not None:
            return False
        
        p_queue = []
        q_queue = []
        
        while p is not None and q is not None:
            if p.val != q.val:
                return False
            
            left_children = self.add_child_to_lists(p.left, p_queue, q.left, q_queue)
            right_children = self.add_child_to_lists(p.right, p_queue, q.right, q_queue)
            
            if not left_children or not right_children:
                return False
            
            p = p_queue.pop() if len(p_queue) > 0 else None
            q = q_queue.pop() if len(q_queue) > 0 else None
        
        return True
