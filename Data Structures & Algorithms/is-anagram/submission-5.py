class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        CountT = {}
        CountS = {}

        for c in s:
            CountT[c] = CountT.get(c,0) + 1
        for c in t:
            CountS[c] = CountS.get(c,0) + 1

        if CountT == CountS:
            return True
        else:
            return False