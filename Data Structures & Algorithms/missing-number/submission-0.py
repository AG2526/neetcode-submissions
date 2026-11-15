class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2    # sum of 0..n
        return expected - sum(nums)    # the difference is the missing number