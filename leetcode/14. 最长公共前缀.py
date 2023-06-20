class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        count = 201
        for i in range(len(strs)):
            if len(strs[i]) < count:
                count = len(strs[i])
        res = ''
        for i in range(count):
            tmps = strs[0][i]
            tag = 0
            for j in range(1, len(strs)):
                if strs[j][i] == tmps:
                    continue
                else:
                    tag = 1
                    break
            if tag == 0:
                res += tmps
        print(res)



strs = ["flower","flow","flight"]
ss = Solution()
ss.longestCommonPrefix(strs)