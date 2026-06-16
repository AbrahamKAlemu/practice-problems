class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        for i in range(len(intervals) - 1):
            prev, nxt = intervals[i], intervals[i + 1]
            if prev[1] > nxt[0]:
                if prev[1] < nxt[1]:
                    nxt[1] = prev[1]
                count += 1
        return count