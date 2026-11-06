class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #dp[i] = length of the longest increasing subsequence ending at 
        #index i.Everything starts at 1, since a single element is a valid
        #subsequence 
        dp = [1]*len(nums)
        for i in range(len(nums)):
            #now look at every element before i 
            for j in range(i):
                #strictly increasing: nums[j] must be smaller than nums[i]
                if nums[j]<nums[i]: 
                    #we can extend the subsequence ending at j by adding 
                    #nums[i] 
                    dp[i] = max(dp[i],dp[j]+1)

        #best subsequence could end at any index so take the max 
        return max(dp) 
        
