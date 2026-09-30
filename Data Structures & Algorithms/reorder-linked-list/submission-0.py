# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #put the nodes in an array as it can be indexed 
        nodes = []
        curr = head 
        while curr: 
            nodes.append(curr) 
            curr = curr.next
        i,j = 0 ,len(nodes) -1 
        while i < j: 
            nodes[i].next = nodes[j] 
            i+=1 
            if i == j: 
                break 
            nodes[j].next = nodes[i]
            j-=1
        nodes[i].next= None # the middle node is at the end and so set the next pointer to null and without this we will get it to point to what it previously pointed to 
        