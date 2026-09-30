# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find the middle using the slow and fast pointer method 
        slow,fast = head,head.next
        while fast and fast.next: 
            slow= slow.next 
            fast = fast.next.next 
        #cut the list and reverse the second half 
        second = slow.next 
        slow.next =None 
        prev =None 
        while second: 
            temp= second.next 
            second.next = prev 
            prev= second 
            second = temp 
        second = prev 
        #weave both halves together 
        first = head 
        while second: 
            tmp1,tmp2= first.next ,second.next 
            first.next = second 
            second.next = tmp1
            first,second = tmp1,tmp2 
            