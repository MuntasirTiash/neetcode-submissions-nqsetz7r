class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr_max = 0 
        all_max = 0
        for n in nums:
            if n == 1:
                curr_max +=1
                if curr_max > all_max:
                    all_max = curr_max

            else:
                curr_max = 0

        return all_max