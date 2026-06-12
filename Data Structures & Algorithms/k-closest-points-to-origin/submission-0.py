import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        e = len(points)
        sorted_points = self.quicksort(points,0,e-1)
        return sorted_points[:k]

    def quicksort(self,points,s,e):
        if e-s+1 <=1:
            return points
    
        pivot = points[e]
        left = s

        for i in range(s,e):
            x1,y1 = points[i]
            x2,y2 = pivot
            if self.distance(x1,y1) < self.distance(x2,y2):
                tmp = points[i]
                points[i] = points[left]
                points[left] = tmp
                left+=1

        
        points[e] = points[left]
        points[left] = pivot

        self.quicksort(points,s,left-1)
        self.quicksort(points,left+1,e)

        return points



    
    def distance(self,x1,y1):
        return (math.sqrt(x1**2+y1**2))
        