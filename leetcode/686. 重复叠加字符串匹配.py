class Solution(object):
    def repeatedStringMatch(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        # 执行用时：132ms, 在所有Python提交中击败了68.75 %的用户
        if b in a:
            return 1
        count = 2
        index = 2
        setn = set(b)
        for sn in setn:
            if sn not in a:
                return -1
        while 1:
            if len(a * index) > len(b) * 25:
                return -1
            if b in a * index:
                return count
            else:
                index += 1
                count += 1

a = "abcd"
b = "cdabcdab"
ss = Solution()
print(ss.repeatedStringMatch(a, b))