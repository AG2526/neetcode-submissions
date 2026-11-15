class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        # dp[i] = best sum of a subarray ending exactly at index i
        dp = [0] * n
        dp[0] = nums[0]                # only one choice for the first element

        for i in range(1, n):          # start at 1, since index 0 is done
            # extend the previous subarray, or start a new one at nums[i]
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        # the best subarray ends somewhere, so take the max over all positions
        return max(dp)