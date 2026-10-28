class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-s for s in stones]
        heapq.heapify(heap)#this turns the list we have into a heap in O(n) 
        while len(heap) >1: #require two stones to smash
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap) #second heaviest 
            if y != x: 
                heapq.heappush(heap,-(y-x))
        return -heap[0] if heap else 0 
    
        