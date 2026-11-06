class Solution:
    def climbStairs(self, n: int) -> int:
        # to land on step n your last move was either a 1 step from n-1 or
        # a 2 step from n-2  so use recursion ways(1) =1 one step only 1 
        # ways(2) =2 as it is 1+1 or 2 
        #memo is a dictionary : key = step number, value = number of ways 
        #stats empty and fills up as we compute answers 
        memo = {}
        #have a helper function nested inside so it can see 'memo'
        def ways(k): 
            #base case 
            if k <=2:
                return k 
            if k in memo:
                return memo[k]
            #otherwise compute it,save it and return it 
            memo[k] = ways(k-1) +ways(k-2) 
            return memo[k] 
        return ways(n)

        
        