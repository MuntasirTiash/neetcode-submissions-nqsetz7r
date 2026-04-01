class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr_max = -1
        res = [-1] * len(arr)
        for i in range(len(arr)-1,0,-1):
            if curr_max < arr[i]:
                curr_max = arr[i]
            res[i-1]=curr_max


        return res