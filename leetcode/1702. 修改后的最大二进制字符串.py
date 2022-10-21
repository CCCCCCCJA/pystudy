class Solution(object):
    def maximumBinaryString(self, binary):
        """
        :type binary: str
        :rtype: str
        """
        res = ''
        len_len = len(binary)
        for i in range(len_len-1):
            tmp = binary[i] + binary[i+1]
            # print(tmp)
            if tmp == '00':
                res += '1'
            elif tmp == '10':
                res += '0'
            else:
                res += binary[i]
        print(res)

binary = "000110"
ss = Solution()
ss.maximumBinaryString(binary)