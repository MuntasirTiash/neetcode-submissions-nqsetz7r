class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        HashMap = {}
        i = 0
        for num in nums:
            if target - num in HashMap:
                return [HashMap[target-num],i]
            else:
                HashMap[num] = i

            i+=1