class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda interval:interval[0])

        res = []

        if len(intervals) == 1:
            return intervals

        for i in range(len(intervals)-1):
            if intervals[i+1][0] <= intervals[i][1]:
                intervals[i+1] = [min(intervals[i][0],intervals[i+1][0]), max(intervals[i][1],intervals[i+1][1])]
            else:
                res += intervals[i:i+1]

        res.append(intervals[i+1])
        return res