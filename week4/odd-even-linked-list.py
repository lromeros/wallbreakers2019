# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None:
            # less than 3 nodes in the list, already in order
            return head
        else:
            i = 1
            odd_nodes = []
            even_nodes = []
            
            while head is not None:
                node_list = even_nodes if i % 2 == 0 else odd_nodes
                if len(node_list) > 0:
                    node_list[-1].next = head
                node_list.append(head)
                head = head.next
                i += 1
                
            odd_nodes[-1].next = even_nodes[0]
            even_nodes[-1].next = None
            
            return odd_nodes[0]
            
