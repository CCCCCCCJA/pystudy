class Solution(object):
    def countPrimeSetBits(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        tmp = []
        for i in range(left, right+1):

            tmp.append(bin(i).count('1'))
        print(tmp)
        count = 0
        for nn in tmp:
            if nn == 1:
                continue
            for i in range(2, nn):
                if (nn % i) == 0:
                    break
            else:
                count += 1
        print(count)
        return count



left = 6
right = 10
ss = Solution()
ss.countPrimeSetBits(left, right)
