class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #handle the edge case which is when the substring t is empty 
        if t == "": return ""
        # have two windows which are both going to be hashmaps 
        countT, window = {},{}
        #start by initialising the countT map as this won't change 
        for c in t: 
            countT[c] = 1 + countT.get(c,0)
        #declare variables have and need which we use to compare countT and window 
        #len of countT will give us distinct variables in t
        have,need = 0, len(countT)
        res,resLen = [-1,-1], float("infinity") 
        l=0 
        #iterate through s with a right pointer r
        for r in range(len(s)):
            c=s[r]
            window[c] = 1 + window.get(c,0)
            #check if the character in s matches t and if true then we can increment have by 1 
            if c in countT and window[c] == countT[c]: 
                have+=1 
            
            #check if have == need and use a while loop. Update res if have == need 
            while have == need: 
                if (r-l+1)< resLen: 
                    res = [l,r]
                    resLen= (r-l+1) 
                #while this is true try to minimise the window by popping the elements 
                window[s[l]]-=1 
                if s[l] in countT and window[s[l]]< countT[s[l]]: 
                    have -=1 
                l+=1 #after this we will check while condition 
        l,r = res 
        #then return the substring of l to r if our resLen has changed as it's possible if it hasn't changed 
        return s[l:r+1]if resLen!= float("infinity") else "" 
        

                

        

