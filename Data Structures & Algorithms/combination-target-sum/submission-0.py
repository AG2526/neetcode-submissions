class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [] #stores the valid combinations we have so far 
        path=[] #the current path we are on in terms of producing a combination 

        def dfs(i,remaining): 
            if remaining ==0 : 
                res.append(path.copy())
                return 
            if i == len(nums) or remaining < 0: 
                return 
            path.append(nums[i])
            dfs(i,remaining - nums[i])
            path.pop()
            dfs(i+1,remaining)
        dfs(0,target)
        return res 
        