class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) ==1: 
            return nums[0]
        def rob_line(houses): 
            prev1 = 0 
            prev2 = 0
            for num in houses: 
                current = max(prev1,num+prev2)
                prev2= prev1
                prev1 = current 
            return prev1 
        return max(rob_line(nums[:-1]),rob_line(nums[1:]))