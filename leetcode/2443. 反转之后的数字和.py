class Solution(object):
    def sumOfNumberAndReverse(self, num):
        """
        :type num: int
        :rtype: bool
        """
        for i in range(num):
            reint = int(str(i)[::-1])
            if reint > num:
                continue
            else:
                if reint + i == num:
                    return True
        return False


ss = Solution()
print(ss.sumOfNumberAndReverse(181))