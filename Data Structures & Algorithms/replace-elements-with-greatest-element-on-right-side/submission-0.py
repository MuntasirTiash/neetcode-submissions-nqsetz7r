class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            curr_max = 0
            for j in range(i+1,len(arr)):
                if curr_max < arr[j]:
                    curr_max = arr[j]

            arr[i] = curr_max

        arr[-1] = -1

        return arr 
