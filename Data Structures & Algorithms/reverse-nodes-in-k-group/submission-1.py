# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head) #get the length of our linked list 
        groups = length//k #this will deal with leftovers since it's integer division
        dummy = ListNode(0,head)
        groupPrev = dummy # the node just before the current group 
        for _ in range(groups): 
            prev = None 
            cur = groupPrev.next #first node of the group 
            
            #now reverse k nodes within the group 
            for _ in range(k): 
                nxt = cur.next
                cur.next = prev 
                prev = cur 
                cur = nxt 
            tail = groupPrev.next # old first node now becomes the group's tail 
            tail.next = cur #connect the tail to the start of the next group 
            groupPrev.next =prev #node before the group connects to the new front 
            groupPrev = tail 
        return dummy.next 
    def getLength(self,head): 
        count = 0 
        cur = head 
        while cur: 
            count+=1 
            cur =cur.next 
        return count 

        