class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')

            if rem in cache:
                return cache[rem]

            res = float('inf')

            for coin in coins:
                res = min(res, 1 + dfs(rem - coin))

            cache[rem] = res
            return cache[rem]

        ans = dfs(amount)
        return -1 if ans == float('inf') else ans