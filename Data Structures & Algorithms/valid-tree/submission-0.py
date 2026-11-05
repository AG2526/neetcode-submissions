class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #a tree with n nodes must have exactly n-1 edges 
        if len(edges) != n-1: 
            return False
        
        #build an adjacency list 
        adj = [[]for _ in range(n)]
        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)
        visited = set()
        def dfs(node): 
            visited.add(node)
            for nei in adj[node]:
                if nei not in visited: 
                    dfs(nei)
        dfs(0)
        return len(visited) == n 
        