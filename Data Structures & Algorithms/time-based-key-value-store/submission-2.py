class TimeMap:

    def __init__(self):
        #initialise key ,value and timestamp
        self.store  = defaultdict(list) #initialise the dictionary no template required  

         
       
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.store[key].append((timestamp,value))
        

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store : 
            return ""
        entries = self.store[key] 
        lo, hi = 0 , len(entries) -1 
        res = "" 
        while lo <= hi : 
            mid = (lo+hi)//2 
            if entries[mid][0]<= timestamp:
                res= entries[mid][1]
                lo = mid+1 #try and find a later one 
            else: 
                hi= mid -1 
        return res  
