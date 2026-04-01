class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]:
                return False

        return True