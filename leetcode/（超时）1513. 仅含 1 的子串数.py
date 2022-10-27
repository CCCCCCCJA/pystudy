class Solution(object):
    def numSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = s.count('1')
        len_len = len(s)
        for i in range(2, len_len+1):
            for j in range(len_len):
                tmps = s[j:j+i]
                if (len(tmps) == i) & (tmps == '1' * i):
                    count += 1
                    continue
                if len(tmps) != i:
                    break
        # print(count)
        return count


s = '111111'
ss = Solution()
ss.numSub(s)