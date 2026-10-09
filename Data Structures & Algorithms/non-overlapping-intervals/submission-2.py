class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda intervals: intervals[1])

        count = 1
        n = len(intervals)
        last_end = intervals[0][1]
        for i in range(len(intervals)-1):
            if intervals[i+1][0] >= last_end:
                last_end = intervals[i+1][1]
                count+=1

        return n - count 