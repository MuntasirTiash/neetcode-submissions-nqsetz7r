class Solution:
    def countSubstrings(self, s: str) -> int:
        res = []
        resNum = 0

        for i in range(len(s)):
            # odd numbers palindrome
            l,r = i,i
            while l>=0 and r < len(s) and s[l]==s[r]:
                resNum+=1
                l-=1
                r+=1
            # Even numbers palindrome
            l,r = i,i+1
            while l>=0 and r < len(s) and s[l]==s[r]:
                resNum+=1
                l-=1
                r+=1

        return resNum