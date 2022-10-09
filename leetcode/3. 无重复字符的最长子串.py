class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = []
        len_s = len(s)
        len_tmp = len(tmp)
        for i in range(len_s):
            for j in range(i, len_s):
                if s[j] not in tmp:
                    tmp.append(s[j])
                else:
                    break
            if len(tmp) > len_tmp:
                len_tmp = len(tmp)
            tmp = []
            print('----')
        print(tmp)
        print(len_tmp)
        return len_tmp


s = 'abcabcbb'
ss = Solution()
ss.lengthOfLongestSubstring(s)