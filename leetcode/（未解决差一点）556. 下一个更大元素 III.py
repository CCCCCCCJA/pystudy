class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        strn = str(n)
        listn = list(strn)
        listn = listn[::-1]
        for i in range(len(listn)-1):
            if listn[i] > listn[i+1]:
                tmp = listn[i]
                listn[i] = listn[i+1]
                listn[i+1] = tmp
                tmp = listn[i+1]
                reslist = listn[i+1:]
                resortlist = listn[:i+1]
                print(reslist, resortlist)
                resortlist.append(tmp)
                resortlist.sort()
                print(resortlist)
                print(listn[i])
                if resortlist[0] == listn[i]:
                    tmp = resortlist[0]
                    resortlist[0] = resortlist[1]
                    resortlist[1] = tmp
                if resortlist[0] < listn[i]:
                    for j in range(len(resortlist)):
                        print(resortlist[i])
                        if resortlist[i] > listn[i]:
                            tmp = resortlist[0]
                            resortlist[0] = resortlist[i]
                            resortlist[i] = tmp
                            break
                print(resortlist)
                resreslist = resortlist[::-1] + reslist[1:]
                print(resreslist)
                resreslist = resreslist[::-1]
                print(resreslist)
                res = int(''.join(resreslist))
                if (res > n) & (res <= 2**31 -1):
                    return res
                else:
                    return -1
        return -1

n = 230241
ss = Solution()
print(ss.nextGreaterElement(n))