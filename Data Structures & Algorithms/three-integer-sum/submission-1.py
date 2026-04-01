class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums_sort = sorted(nums)

        for i in range(len(nums_sort)-2):
            if i > 0 and nums_sort[i] == nums_sort[i-1]:
                continue
            target = nums_sort[i]
            
            l = i+1
            r = len(nums_sort) -1
            while l < r:
                if (target + nums_sort[l] + nums_sort[r]) < 0:
                    l+=1
                elif (target + nums_sort[l] + nums_sort[r]) > 0:
                    r-=1
                elif (target + nums_sort[l] + nums_sort[r]) == 0:
                    res.append([target,nums_sort[l],nums_sort[r]])
                    l+=1
                    while l < r and nums_sort[l] == nums_sort[l-1]:
                        l+=1


        return res