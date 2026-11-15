class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0                      # furthest index reachable so far

        for i in range(len(nums)):        # visit each index left to right
            if i > farthest:              # this index is out of reach
                return False

            # from index i we can land as far as i + nums[i]
            farthest = max(farthest, i + nums[i])

        return True                       # never got stuck, so the end is reachable