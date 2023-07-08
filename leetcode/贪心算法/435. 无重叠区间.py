class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        intervals.sort()
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] >= intervals[i-1][1]:
                continue
            else:
                count += 1
                intervals[i][1] = min(intervals[i][1], intervals[i-1][1])
        # print(count)
        return count

intervals = [ [1,2], [1,2], [1,2] ]
ss = Solution()
ss.eraseOverlapIntervals(intervals)