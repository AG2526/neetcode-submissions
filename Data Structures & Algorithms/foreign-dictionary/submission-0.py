class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        #adj[c]= set of letters that must come after c even ones with no
        #edges so we create an entry for each letter up front 
        adj = {c: set() for word in words for c in word }

        #indegree[c] = number of letters that must come BEFORE c 
        indegree ={c : 0 for c in adj}
        for i in range(len(words)-1): 
            w1,w2 = words[i],words[i+1]
            min_len = min(len(w1),len(w2))
            
            #prefix trap: w1 is longer than w2
            if len(w1) >len(w2) and w1[:min_len] == w2[:min_len]:
                return "" 
            
            for j in range(min_len): 
                if w1[j] != w2[j]: 
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1 
                    break
        queue = deque(c for c in indegree if indegree[c] == 0)
        result = []
        while queue: 
            c = queue.popleft() 
            result.append(c) 
            for nxt in adj[c]: 
                indegree[nxt] -=1 
                if indegree[nxt] == 0 : 
                    queue.append(nxt)
        if len(result) != len(adj):
            return "" 
        return "".join(result) 
        

        