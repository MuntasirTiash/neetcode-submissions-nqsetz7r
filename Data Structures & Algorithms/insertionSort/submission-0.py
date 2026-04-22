class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        n = len(pairs)

        for i in range(0, n):
            j = i - 1
            while (j >= 0 and pairs[j+1].key < pairs[j].key):
                tmp = pairs[j+1]
                pairs[j+1] = pairs[j]
                pairs[j] = tmp
                j = j - 1
            
            res.append(list(pairs[:]))

        return res