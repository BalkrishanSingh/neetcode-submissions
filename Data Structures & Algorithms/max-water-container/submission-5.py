class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        def Compute_Area(i,j,heights):
            area = (j-i) * min(heights[i],heights[j])
            return area
        result = []
        i = 0
        j = len(heights) - 1
        maxArea = Compute_Area(i,j,heights)
       
        while i<j:
            if heights[i] < heights[j]:
                dx,dy = (1,0)
            else:
                dx,dy = (0,1)
            i += dx
            j -= dy
            print(i,j)
            if (area:= Compute_Area(i,j,heights))> maxArea:
                maxArea = area
                
            
        return maxArea
        


