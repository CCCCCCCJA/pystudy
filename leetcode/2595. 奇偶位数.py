class Solution(object):
    def evenOddBit(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        m = ''
        while n > 0:
            m += str(n % 2)  # a对2求余，添加到字符串m最后
            n = n // 2
        # print(m[::-1])  # 反向输出
        m = m[::-1]
        evenCount = 0
        oddCout = 0
        for i in range(len(m)):
            if m[i] != 0:
                if (i + 1) % 2 == 0:
                    oddCout += 1
                else:
                    evenCount += 1
        return [evenCount, oddCout]







ss = Solution()
ss.evenOddBit(17)