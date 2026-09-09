class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        HashMap = {}

        n = len(nums)

        for num in nums:
            HashMap[num] = HashMap.get(num,0) + 1
            if HashMap[num] > n //2:
                return num

