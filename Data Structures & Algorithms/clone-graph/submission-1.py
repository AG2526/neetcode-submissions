"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #edge case: an empty graph with no starting node has nothing to copy 
        if not node: 
            return None 
        #map each original node to its copy 
        old_to_new = {}
        #return the copy of 'old' which creates it and the connections of it 
        def dfs(old): 
            #if already copied then return the copy 
            #this will prevent infinite loops and any duplicate copies 
            if old in old_to_new: 
                return old_to_new[old]
            #if not copied then make a new node with the same value
            #neighbours will start as empty 
            copy = Node(old.val)
            #register copy before exploring neighbours as if we waited 
            #then a neighbour pointing back at 'old' wouldn't find it in
            #map and we'd loop forever 
            old_to_new[old] = copy  
            #go through the original neighbour 
            for nei in old.neighbors : 
                #dfs(nei) will return a copy of that neighbour .attach it 
                #to our copy's neighbours list 
                copy.neighbors.append(dfs(nei))
            #hand the finished copy 
            return copy 
        return dfs(node)
        