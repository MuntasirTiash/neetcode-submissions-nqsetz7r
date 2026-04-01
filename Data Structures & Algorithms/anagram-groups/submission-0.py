class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for l in strs:
            res["".join(sorted(l))].append(l)

        return list(res.values())