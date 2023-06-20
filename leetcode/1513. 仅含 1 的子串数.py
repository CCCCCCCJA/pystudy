class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        lists = s.split('0')
        for i in range(len(lists)):
            lenlen = len(lists[i])
            index = 1
            tmp = 0
            while index <= lenlen:
                tmp += index
                index += 1
            count += tmp % (10**9+7)
        print(count)
        return count



s = '0110111'
ss = Solution()
ss.numSub(s)