class MedianFinder:

    def __init__(self):
        self.small = [] #max-heap stored as negatives 
        self.large = [] #min-heap 

        

    def addNum(self, num: int) -> None:
        #add the number into the small pile 
        heapq.heappush(self.small,-num) 
        #move the biggest of small into large 
        biggest_of_small = -heapq.heappop(self.small)
        heapq.heappush(self.large,biggest_of_small)
        #keep the piles balanced 
        if len(self.large) > len(self.small): 
            smallest_of_large = heapq.heappop(self.large) 
            heapq.heappush(self.small, -smallest_of_large)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            #odd count so small has the extra one 
            return float(-self.small[0])
        return (-self.small[0] +self.large[0])/2.0
        
        