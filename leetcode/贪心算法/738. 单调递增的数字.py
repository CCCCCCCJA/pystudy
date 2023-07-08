class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 内存超出
        # if n < 10:
        #     return n
        # for i in range(n, 0, -1):
        #     if n == 10:
        #         return 9
        #     tmpn = str(i)
        #     for j in range(1, len(tmpn)):
        #         # print(tmpn[j], tmpn[j-1])
        #         if tmpn[j] >= tmpn[j-1]:
        #             continue
        #         else:
        #             break
        #     else:
        #         return i
        # 16ms
        strn = str(n)
        flag = len(strn)
        for i in range(len(strn)-1, 0, -1):
            if strn[i-1] > strn[i]:
                strn = strn[:i-1] + str(int(strn[i-1])-1) + strn[i:]
                flag = i
        # print(strn, flag)
        res = strn[:flag] + '9' * (len(strn) - flag)
        return int(res)
n = 10
ss = Solution()
print(ss.monotoneIncreasingDigits(n))