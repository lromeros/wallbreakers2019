# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        node_values = []
        value_to_node = {}

        for node in lists:
            while node is not None:
                node_values.append(node.val)
                if value_to_node.get(node.val) is None:
                    value_to_node[node.val] = [node]
                else:
                    value_to_node[node.val].append(node)
                node = node.next
                
        if len(node_values) > 0:
            heapq.heapify(node_values)
            current_value = heapq.heappop(node_values)
            head = value_to_node.get(current_value).pop()
            current_node = head
            
            while len(node_values) > 0:
                next_node = value_to_node.get(heapq.heappop(node_values)).pop()
                current_node.next = next_node
                current_node = next_node
                if len(node_values) == 0:
                    next_node.next = None

            return head

