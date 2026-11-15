class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)                 # start with n (it's in the range but never an index)

        for i in range(len(nums)):
            result ^= i ^ nums[i]          # XOR in the index and the value

        return result