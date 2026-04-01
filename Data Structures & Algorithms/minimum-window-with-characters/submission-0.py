class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        countS = {}
        countT = {}

        res = ''

        for r in range(len(t)):
            countT[t[r]] = countT.get(t[r],0) + 1

        least = 1001
        for r in range(len(s)):
            countS[s[r]] = countS.get(s[r],0) + 1
            
            while all(countS.get(char, 0) >= freq for char, freq in countT.items()):
                if r - l + 1 < least:
                    least = r - l + 1
                    res = s[l:r+1]
                
                countS[s[l]] -= 1
                l += 1
        return res