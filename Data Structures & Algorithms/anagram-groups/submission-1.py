from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list) # here the default value is an empty list 
        for word in strs: 
            key = tuple(sorted(word))
            groups[key].append(word) 
        return list(groups.values())