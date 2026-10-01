class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diffs = {}

        for idx in range(len(nums)):
            diff = target - nums[idx]
            if nums[idx] in diffs:
                return [diffs[nums[idx]], idx]
            else:
                diffs[diff] = idx