class Solution(object):
    def huoqu(self, num, len_num):
        num_list = []
        tag = 1
        while len_num:
            num_list.append(int(num/tag) % 10)
            len_num -= 1
            tag *= 10
        return num_list
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        tmp = num
        len_num = len(str(num))
        tag = 1
        sum = 0
        num_list = self.huoqu(num, len_num)
        while len_num:
            num_list.append(int(tmp/tag) % 10)
            len_num -= 1
            tag *= 10
        for n in num_list:
            sum += n
        if sum > 10:
            len_num = len(str(sum))
            
        print(num_list)
        print(sum)


num = 38
ss = Solution()
ss.addDigits(num)