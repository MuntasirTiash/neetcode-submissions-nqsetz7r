class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d = [x for row in matrix for x in row]

        print(one_d)

        L, R = 0, len(one_d) - 1 

        while L <= R:
            mid = (L+R)//2
            if target > one_d[mid]:
                L = mid + 1
            elif target < one_d[mid]:
                R = mid - 1
            else:
                return True
        
        return False
