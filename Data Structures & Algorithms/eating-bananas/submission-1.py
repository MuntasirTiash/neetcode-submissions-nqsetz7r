class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        res = max(piles)
        
        while low <= high:
            mid = (low+high)//2

            if self.total_time(piles,mid) <= h:
                res = min(res, mid)
                high = mid - 1
            elif self.total_time(piles,mid) > h:
                low = mid + 1
            
        return res

            


    def total_time(self,piles,k):

        total = 0

        for pile in piles:
            total = total + -(pile//-k) 

        return total 