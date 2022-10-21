class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        res = ''
        tmp_num = n
        tmp_tmp = 0
        count = 0
        while tmp_num != 1:
            if count > 20:
                return False
            tmp = list(str(tmp_num))
            for i in range(len(tmp)):
                tmp[i] = int(tmp[i]) ** 2
                tmp[i] = str(tmp[i])
            for n in tmp:
                tmp_tmp += int(n)
            tmp_num = tmp_tmp
            tmp_tmp = 0
            count += 1
        return True

n = 19
ss = Solution()
ss.isHappy(n)
