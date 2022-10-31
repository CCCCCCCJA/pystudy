class Solution(object):
    def longestWPI(self, hours):
        """
        :type hours: List[int]
        :rtype: int
        """
        res = []
        for i in range(len(hours)):
            for j in range(i+1, len(hours)+1):
                tmp = hours[i:j]
                naolei = 0
                nonaolei = 0
                for tn in tmp:
                    if tn > 8:
                        naolei += 1
                    else:
                        nonaolei += 1
                if naolei > nonaolei:
                    res.append(tmp)
        # print(res)
        # if len(res) == 0:
        #     return 0
        # dict1 = {}
        # for i in range(len(res)):
        #     lenlen = len(res[i])
        #     dict1[i] = lenlen
        # print(max(dict1))
        # return max(dict1)
        count = []
        for rs in res:
            count.append(len(rs))
        print(max(count))
        return max(count)
hours = [6,6,9]
ss = Solution()
ss.longestWPI(hours)
