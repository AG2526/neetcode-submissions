class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[]for _ in range(numCourses)]
        for course,prereq in prerequisites: 
            adj[course].append(prereq)
        state = [0]*numCourses
        def has_cycle(c):
            if state[c] ==1 : 
                return True 
            if state[c] ==2 : 
                return False 
            state[c] =1 
            for p in adj[c]: 
                if has_cycle(p): 
                    return True
            
            state[c] =2
            return False 

        for c in range(numCourses): 
            if has_cycle(c):  
                return False 
        return True 

        