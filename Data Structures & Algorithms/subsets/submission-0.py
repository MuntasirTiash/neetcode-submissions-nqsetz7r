class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            # case to include i
            subset.append(nums[i])
            print(subset)
            dfs(i+1)

            # case to not include i
            subset.pop()
            print(subset)
            dfs(i+1)

        dfs(0)

        return res