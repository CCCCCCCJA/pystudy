class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        print(x)
        print(2**31-1)
        if x == 0:
            return 0
        tmpx = abs(x)
        strx = str(tmpx)
        strx = strx[::-1]
        tmpstr = str(2**31-1)
        print(strx)
        if len(strx) < len(tmpstr):
            if x > 0:
                return int(strx)
            else:
                return int(strx) * -1
        elif len(strx) > len(tmpstr):
            return 0
        else:
            count = 0
            if x > 0:
                for i in range(len(strx)):
                    if strx[i] < tmpstr[i]:
                        continue
                    elif strx[i] == tmpstr[i]:
                        count += 1
                    else:
                        if count == i:
                            return 0
                        else:
                            return int(strx)
                return int(strx)
            else:
                for i in range(len(strx)):
                    if strx[i] < tmpstr[i]:
                        continue
                    elif strx[i] == tmpstr[i]:
                        count += 1
                    else:
                        if count == i:
                            return 0
                        else:
                            return int(strx) * -1
                return int(strx) * -1

x = 1563847412
ss = Solution()
print(ss.reverse(x))
