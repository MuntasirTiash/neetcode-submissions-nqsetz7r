class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sums_array = []
        for i in range(len(nums)):
            sums = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                sums = sums* nums[j]
            sums_array.append(sums)

        return sums_array
        