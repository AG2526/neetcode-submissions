class Solution:
    def rob(self, nums: List[int]) -> int:
        #prev1 = best total using houses up to the previous house (i-1) 
        #prev2 = best total using houses up to two houses back (i-2) 
        #both start at 0 because no houses are processed and so we have 
        # robbed nothing 
        prev1 = 0 
        prev2 = 0 
        #go through each house's money one at a time ,left to right 
        #num is the money is the money in the current house 
        for num in nums: 
            #either skip the house and keep the best so far(prev1) 
            #rob this house which is num+ best from two houses back 
            #take the bigger of the two 
            current = max(prev1, num+prev2)
            prev2 = prev1 
            prev1 = current 
        return prev1
        