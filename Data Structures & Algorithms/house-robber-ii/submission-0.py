class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        def rob_linear(houses):
            cache = {}
            def memo(i):
                if i >= len(houses):
                    return 0
                if i in cache:
                    return cache[i]
                cache[i] = max(houses[i] + memo(i + 2), memo(i + 1))
                return cache[i]
            return memo(0)
        return max(rob_linear(nums[1:]), rob_linear(nums[:-1]))