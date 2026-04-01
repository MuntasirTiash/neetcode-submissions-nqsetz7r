class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        if len(nums) == 0:
            return False

        for num in nums:
            hashset[num] = hashset.get(num,0) + 1

        if max(hashset.values()) > 1:
            return True
        else:
            return False