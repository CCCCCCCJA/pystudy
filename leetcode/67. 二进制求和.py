class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # 执行用时：24ms
        lena = len(a)
        lenb = len(b)
        i = lena - 1
        j = lenb - 1
        res = []
        tag = 0
        while i >= 0 and j >= 0:
            if int(a[i]) + int(b[j]) == 2:
                res.append(str(tag))
                tag = 1
            elif int(a[i]) + int(b[j]) == 1:
                if tag == 0:
                    res.append('1')
                else:
                    res.append('0')
                    tag = 1
            else:
                res.append(str(tag))
                tag = 0
            i -= 1
            j -= 1
        if i >= 0:
            while i >= 0:
                if tag + int(a[i]) == 2:
                    res.append('0')
                elif tag + int(a[i]) == 1:
                    res.append('1')
                    tag = 0
                else:
                    res.append('0')
                    tag = 0
                i -= 1
        if j >= 0:
            while j >= 0:
                if tag + int(b[j]) == 2:
                    res.append('0')
                elif tag + int(b[j]) == 1:
                    res.append('1')
                    tag = 0
                else:
                    res.append('0')
                    tag = 0
                j -= 1
        if i < 0 and j < 0:
            if tag == 1:
                res.append('1')

        return ''.join(res[::-1])


a = "1010"
b = "1011"
ss = Solution()
print(ss.addBinary(a, b))