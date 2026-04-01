class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Counts = {}
        Countt = {}

        for c in s:
            Counts[c] = Counts.get(c,0)+1

        for c in t:
            Countt[c] = Countt.get(c,0)+1

        if Counts == Countt:
            return True
        else:
            return False