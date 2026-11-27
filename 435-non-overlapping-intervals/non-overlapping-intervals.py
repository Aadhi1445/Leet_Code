class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        c=0
        intervals.sort()
        for i in range(len(intervals)-1):
            if intervals[i][1]>intervals[i+1][0]:
                c+=1
                intervals[i+1][1]=min(intervals[i][1],intervals[i+1][1])
            else:
                pass
                # intervals[i+1][0]=intervals[i][1]
        return c
        