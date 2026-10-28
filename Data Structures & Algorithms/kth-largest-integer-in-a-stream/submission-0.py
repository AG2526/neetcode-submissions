class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k #remember for later calls 
        self.heap =[]
        for n in nums: 
            self.add(n) 
        

    def add(self, val: int) -> int:
        if len(self.heap)<self.k: 
            heapq.heappush(self.heap,val)
        elif val >self.heap[0]:
            heapq.heapreplace(self.heap,val)
        return self.heap[0]
        
