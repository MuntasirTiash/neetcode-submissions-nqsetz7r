class Solution:
    def rob(self, nums: List[int]) -> int:
        total = len(nums)
        memo = {}

        def dfs(curr_index):
            if curr_index >= total:
                return 0
            if curr_index in memo:
                return memo[curr_index]

            memo[curr_index] = max(nums[curr_index] + dfs(curr_index+2), dfs(curr_index + 1))
            
            return memo[curr_index]
        
        return dfs(0)

