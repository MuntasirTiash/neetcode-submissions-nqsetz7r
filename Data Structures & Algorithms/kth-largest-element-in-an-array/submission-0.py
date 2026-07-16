class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-s for s in nums]

        heapq.heapify(max_heap)

        i = k

        while i>0:
            cur = heapq.heappop(max_heap)
            i-=1

        return -cur
