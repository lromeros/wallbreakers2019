# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        
        last = None
        
        while head is not None:
            _next = head.next
            head.next = last
            last = head
            head = _next
         
        return last
            
