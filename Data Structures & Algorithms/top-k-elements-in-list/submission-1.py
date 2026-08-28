class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)  
        for i in nums:
            a[i]+=1
        
        sorted_nums = sorted(a.keys(), key= lambda x : a[x] ,reverse=True)
        return sorted_nums[:k]

