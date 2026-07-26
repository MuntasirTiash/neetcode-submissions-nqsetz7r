class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        left,right = 0, 0

        for i in range(len(nums)):
            left = i
            right = min(i + k,len(nums)-1)
            while left < right:
                if (nums[left] == nums[right]):
                    return True
                right -=1

            
        return False
                