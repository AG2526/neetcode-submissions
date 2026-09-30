# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set() 
        while head: 
            if head in seen: 
                return True 
            seen.add(head) # store the nodes and not the values as two different nodes can hold the same value 
            head = head.next
        return False 
        # O(n) time complex since each node is visited once 
        # O(n) space complex since the set can hold every ndoe 