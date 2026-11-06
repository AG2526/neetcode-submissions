class Solution:
    def longestPalindrome(self, s: str) -> str:
        #track the best palindrome found so far as [start,end] indices 
        best_start = 0 
        best_len = 0 

        #create a helper function and expand outwards from (left,right) 
        #while it's still a palindrome 
        def expand(left,right): 
            #stay within the string and the characters must match 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                left -=1 
                right+=1 
            #loop stopped: 
            return left+1,right #start and end index 
        for i in range(len(s)): 
            l1,r1 = expand (i,i) #odd length palindromes : centre is the
            #single character i 
            l2,r2 = expand(i,i+1)#even length palindromes: centre is between i and i+1 
            #now compare the lengths of both and keep the longer one 
            if r1 - l1 >best_len:
                best_start,best_len = l1, r1-l1  
            if r2 - l2 > best_len: 
                best_start, best_len = l2,r2- l2 
        return s[best_start : best_start + best_len]


        