class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        l=0
        r = len(heights) - 1
        while l < r:
            area = min(heights[l],heights[r]) * (r-l)

            if max_area < area:
                max_area = area
            
            if heights[l] - heights[r] > 0:
                r-=1
            else:
                l+=1

        return max_area

        