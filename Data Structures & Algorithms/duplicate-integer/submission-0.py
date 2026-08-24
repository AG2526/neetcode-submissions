class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()          # empty set to track numbers we've seen
        
        for n in nums:        # go through each number
            if n in seen:      # already seen it? duplicate found
                return True
            seen.add(n)        # otherwise remember it
        
        return False           # no duplicates found