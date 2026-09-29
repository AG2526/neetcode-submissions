class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if (len(nums1)>len(nums2)):
            return self.findMedianSortedArrays(nums2,nums1)
        
        x = len(nums1) 
        y= len(nums2) 

        start = 0 
        end = x 
        while (start<=end): 
            partX = (start+end)//2
            partY = (x+y+1)//2 - partX 

            xLeft = float('-inf') if partX == 0 else nums1[partX - 1 ]
            xRight = float('inf') if partX == x else nums1[partX]
            yLeft = float('-inf') if partY == 0 else nums2[partY - 1 ]
            yRight = float('inf') if partY == y else nums2[partY]
            if (xLeft <= yRight and yLeft <= xRight):
                if (x+y)%2 == 0 : 
                    return (max(xLeft,yLeft) + min(xRight,yRight))/2
                else: 
                    return max(xLeft,yLeft) 
            elif (xLeft >yRight): 
                end = partX -1 
            else : 
                start = partX + 1 
        return 0 



