"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        answer = []
        stack = [root] if root is not None else []
        
        while len(stack) > 0:
            root = stack.pop()
            
            if len(root.children) > 0:
                stack.extend(root.children)
                
            answer.insert(0, root.val)
                
        return answer
