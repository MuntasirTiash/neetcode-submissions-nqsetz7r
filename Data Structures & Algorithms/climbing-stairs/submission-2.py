class Solution:
    def climbStairs(self, n: int) -> int:
        def memo(s,cache):
            if s == n:
                return 1
            if s > n:
                return 0

            if cache[s] != -1:
                return cache[s]

            cache[s] = memo(s+1,cache) + memo(s+2,cache)

            return cache[s]

        return memo(0,[-1]*(n+1)) 