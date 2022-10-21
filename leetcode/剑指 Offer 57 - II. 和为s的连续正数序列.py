class Solution(object):
    def findContinuousSequence(self, target):
        """
        :type target: int
        :rtype: List[List[int]]
        """
        start = 1
        i = 1
        res = []
        tmp = []
        res_sum = 0
        while 1:
            i = start
            while 1:
                res_sum += i
                if res_sum < target:
                    tmp.append(i)
                if res_sum == target:
                    res.append(tmp)
                if res_sum > target:
                    break
                i += 1
            res_sum = 0
            tmp = []
            start += 1
            if start > target:
                break
        print(res)


target = 9
ss = Solution()
ss.findContinuousSequence(target)
