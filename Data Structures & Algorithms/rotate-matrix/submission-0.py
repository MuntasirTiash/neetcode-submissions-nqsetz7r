class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1

        while (l < r):
            for i in range(r-l):
                top, bottom = l, r
                # store the topLeft
                topLeft = matrix[top][l+i]

                #rotate the top left with the bottom left
                matrix[top][l + i] = matrix[bottom - i][l]

                # rotate the bottom left with the topleft
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # rotate the bottomright with the bottom left
                matrix[bottom][r- i] = matrix[top + i][r]

                # rotate the top right with the top left
                matrix[top + i][r] = topLeft
            l +=1
            r -=1

