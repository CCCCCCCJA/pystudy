class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        res = []
        for i in range(len(num)-2):
            if (num[i] == num[i+1]) & (num[i+1] == num[i+2]):
                print(num[i] + num[i+1] + num[i+2])
                res.append(num[i] + num[i+1] + num[i+2])
        if len(res) == 0:
            return ''
        else:
            return max(res)



num = "2300019"
ss = Solution()
ss.largestGoodInteger(num)