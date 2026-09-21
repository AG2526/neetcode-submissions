class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # start with len of temps and have each one have a default value 
        res = [0] * len(temperatures) 
        stack = [] #pair of values with temp,index
        for i ,t in enumerate(temperatures): 
            while stack and t > stack[-1][0]:
                stackT,stackInd=stack.pop()
                res[stackInd]= (i-stackInd)#add at the corresponding index 
            stack.append([t,i])
        return res 


        