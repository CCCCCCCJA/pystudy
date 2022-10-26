import math


class Solution(object):
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound == 0:
            return []
        if x == 1:
            len_x = 0
        else:
            len_x = int(math.log(bound, x))
        if y == 1:
            len_y = 0
        else:
            len_y = int(math.log(bound, y))
        print(len_x, len_y)
        res = []
        for i in range(0, len_x+1):
            for j in range(0, len_y+1):
                tmp = x ** i + y ** j
                if (tmp <= bound) & (tmp not in res):
                    res.append(tmp)
        print(res)
        return res



x = 2
y = 3
bound = 10
ss = Solution()
ss.powerfulIntegers(x, y, bound)