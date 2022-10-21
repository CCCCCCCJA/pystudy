class Solution(object):
    def addToArrayForm(self, num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        tmp = ''
        for n in num:
            tmp += str(n)
        # print(tmp)
        tmp = list(str(int(tmp) + k))
        for i in range(len(tmp)):
            tmp[i] = int(tmp[i])
        # print(tmp)
        return tmp

num = [1,2,0,0]
k = 34
ss = Solution()
ss.addToArrayForm(num, k)