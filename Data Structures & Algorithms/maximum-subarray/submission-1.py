class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]    # best sum ending at the current position
        best = nums[0]       # best sum seen anywhere so far

        for num in nums[1:]:                   # every element after the first
            current = max(num, current + num)  # extend, or start fresh
            best = max(best, current)          # keep the overall record

        return best