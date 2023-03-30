class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            tmp = i
            tag = 0
            while tmp != 0:
                chushu = tmp % 10
                if chushu == 0:
                    tag = 1
                    break
                if i % chushu == 0:
                    tmp //= 10
                    continue
                else:
                    tag = 1
                    break
            if tag == 0:
                res.append(i)
        print(res)
        return res


left = 1
right = 22
ss = Solution()
ss.selfDividingNumbers(left, right)