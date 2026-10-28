class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #array called points , points stores coordinates x,y
        #use a heap as we go through points and calculate the distance since we want the smallest 
        #store the k smallest points 
        heap = [(x*x + y*y,x,y)for x,y in points]
        heapq.heapify(heap)
        result = []
        for _ in range(k): 
            dist,x,y = heapq.heappop(heap)
            result.append([x,y])
        return result 
        #Time complexity = O(n + klogn) 
        #Space complexity = O(n) 
        

        