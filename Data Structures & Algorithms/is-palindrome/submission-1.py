class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = [c.lower() for c in s if c.isalnum()]

        l, r = 0, len(sl) -1 

        while l < r:
            if sl[l] != sl[r]:
                return False

            l +=1
            r -=1


        return True