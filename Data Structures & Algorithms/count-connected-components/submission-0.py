class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Build the adjacency list. Undirected, so add both directions.
        adj = [[] for _ in range(n)]
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()          # nodes already assigned to a component

        def dfs(node):
            visited.add(node)                # mark before exploring neighbours
            for nei in adj[node]:
                if nei not in visited:       # skip nodes already seen
                    dfs(nei)

        count = 0
        for node in range(n):                # check EVERY node, even ones with no edges
            if node not in visited:          # unvisited means a new component
                count += 1
                dfs(node)                    # mark the whole component as visited

        return count