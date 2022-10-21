class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_str = str(num)
        num_list = list(num_str)
        for i in range(len(num_list)):
            num_list[i] = int(num_list[i])
        max_num = max(num_list)
        index_max = num_list.index(max_num)
        if index_max == 0:
            return num
        num_list[0] = num_list[0] ^ num_list[index_max]
        num_list[index_max] = num_list[0] ^ num_list[index_max]
        num_list[0] = num_list[0] ^ num_list[index_max]
        res = ''
        for n in num_list:
            res += str(n)
        print(res)
        return int(res)


num = 9937
ss = Solution()
ss.maximumSwap(num)