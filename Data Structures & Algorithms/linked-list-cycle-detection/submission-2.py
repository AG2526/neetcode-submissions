# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #use a slow and a fast pointer as if there is a loop then the fast will catch up with the slow 
        slow = head 
        fast = head 
        while fast and fast.next: 
            slow= slow.next 
            fast = fast.next.next 
            if slow is fast: 
                return True 
        return False 
