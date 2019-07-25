# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def adjust_pointers(self, nodes: List[ListNode], k: int):
        for i in range(k):
            nodes[i].next = nodes[i + 1] if i + 1 < k else None
    
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        
        og_head = head 
        first = None
        last = None
        
        while head is not None:
            nodes = [None] * k
            
            for i in range(1, k + 1):
                nodes[i * -1] = head
                head = head.next if head is not None else None
                
            if nodes[0] is not None:
                self.adjust_pointers(nodes, k)
                first = nodes[0] if first is None else first
                if last is not None:
                    last.next = nodes[0]
                last = nodes[-1]
            elif last is not None:
                last.next = nodes[-1]
                
        return first if first is not None else og_head
