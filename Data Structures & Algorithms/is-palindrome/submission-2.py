class Solution:
    def isPalindrome(self, s: str) -> bool:
        #get the length of s and set the middle as the starting point
        # then have a left and right pointer that keep comparing the letters
        #join the letters if they are alnum to ignore spaces and punctuation and make them lower 
        t= "".join(c.lower() for c in s if c.isalnum())
        n = len(t)
        l=(n-1)//2
        r=n//2 
        while l>=0 and r<n: 
            if t[l] != t[r]: 
                return False
            l-=1 
            r+=1 
        return True 