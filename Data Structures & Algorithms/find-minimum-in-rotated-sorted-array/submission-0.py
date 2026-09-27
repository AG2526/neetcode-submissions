class Solution:
    def findMin(self, nums: List[int]) -> int:
        #check if the left pointer is less than the right pointer then do binary search in that range 
        res = nums[0] 
        l,r = 0 , len(nums)-1 
        while l<=r: 
            if nums[l]<nums[r]: 
                res= min(res,nums[l])
                break 
            m = (l+r)//2 
            res = min(res,nums[m])
            if nums[m] >= nums[l]: 
                l=m+1 
            else: 
                r= m-1 
        return res 