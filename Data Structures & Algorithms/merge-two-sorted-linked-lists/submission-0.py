# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #list1 only points to the first node and doesn't hold the whole list 
        # use a dummy node to call .next on and gives the tail something to attach to 
        dummy = ListNode() 
        tail = dummy 
        while list1 and list2: 
            if list1.val< list2.val: 
                tail.next = list1
                list1=list1.next 
            else: 
                tail.next = list2
                list2= list2.next 
            tail= tail.next 
            
        #what if one list still has nodes left 
        tail.next = list1 or list2 # this will add any more nodes if they are not None 
        return dummy.next 