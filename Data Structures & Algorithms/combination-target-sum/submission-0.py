class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            curr_sum = sum(subset)

            if curr_sum == target:
                res.append(subset.copy())
                return
            
            if i >= len(nums) or curr_sum > target:
                return

            # case to include i
            subset.append(nums[i])
            dfs(i)

            # case to not include i
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res 
