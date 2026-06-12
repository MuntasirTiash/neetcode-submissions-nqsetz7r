class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            if not self.check(board[i]):
                return False

        for i in range(9):
            col = [board[j][i] for j in range(9)]
            if not self.check(col):
                return False

        for i in range(0,9,3):
            for j in range(0,9,3):
                square = [board[r][c] for r in range(i, i + 3) for c in range(j, j + 3)]
                if not self.check(square):
                    return False
        
        return True
               
        
    def check(self,r1):
        count={}

        for i in range(1,10):
            count[str(i)]= 0

        for r in r1:
            if r !='.':
                count[r] = count[r]+1
        
        for i in count:
            if count[i] >1:
                return False
        
        return True