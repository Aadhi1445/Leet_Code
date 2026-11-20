class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        result=[intervals[0]]
        for i in range(len(intervals)):
            cl=intervals[i]
            if result[-1][1]<cl[0]:
                result.append(cl)
            else:
                result[-1][1]=max(result[-1][1],cl[1])
        return result

        