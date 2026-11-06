class Solution:
    def countSubstrings(self, s: str) -> int:
        total = 0 #running count of all the palindromic substrings 
        #expand outwards from(left,right) and count every pass that happen

        def expand(left,right): 
            count = 0 #palindromes found from this centre
            #stay inside the string and the characters must match 
            while left >= 0 and right < len(s) and s[left] == s[right]: 
                count+=1 
                left-=1 
                right +=1 
            return count 
        for i in range(len(s)):
            #odd length palindromes:centre is the single char i 
            total+=expand(i,i)
            #even length - centre is the gap between i and i +1 
            total += expand(i,i+1) 
        return total 