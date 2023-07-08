class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        # me 32ms
        # intervals.sort()
        # print(intervals)
        # left = intervals[0][0]
        # right = intervals[0][1]
        # res = []
        # tag = 0
        # # if len(intervals)
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] <= right:
        #         left = min(left, intervals[i-1][0])
        #         right = max(right, intervals[i][1])
        #     else:
        #         res.append([left, right])
        #         left = intervals[i][0]
        #         right = intervals[i][1]
        #         if i == len(intervals)-1:
        #             tag = 1
        # if tag == 1:
        #     res.append([left, right])
        #
        # if len(res) == 0:
        #     res.append([left, right])
        # if res[-1][1] != right:
        #     res.append([left, right])
        # print(res)
        # return res
        # kerl 32ms
        res = []
        if len(intervals) == 0:
            return res
        intervals.sort()
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], intervals[i][1])
            else:
                res.append(intervals[i])
        print(res)
        return res



intervals = [[2,3],[2,2],[3,3],[1,3],[5,7],[2,2],[4,6]]
ss = Solution()
ss.merge(intervals)