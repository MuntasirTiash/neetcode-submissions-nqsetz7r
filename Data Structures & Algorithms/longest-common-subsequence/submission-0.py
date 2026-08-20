class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def memo(i, j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in cache:
                return cache[(i, j)]
            if text1[i] == text2[j]:
                res = 1 + memo(i + 1, j + 1)
            else:
                res = max(memo(i + 1, j), memo(i, j + 1))
            cache[(i, j)] = res
            return res

        return memo(0, 0)