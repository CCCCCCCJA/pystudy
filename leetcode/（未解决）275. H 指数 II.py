class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        l = 0
        r = len(citations) - 1
        iindex = -1
        while l < r:
            middle = (l + r) // 2
            if citations[middle] == len(citations):
                iindex = middle
                break
            elif citations[middle] < len(citations):
                l = middle + 1
            else:
                r = middle - 1
        if iindex != -1:
            tmpIndex = iindex - 1
        else:
            tmpIndex = l - 1
        # print(tmpIndex)
        for i in range(tmpIndex, -1, -1):
            if len(citations) - citations[i] == i:
                h = citations[i]
                return h

citations = [0,1,3,5,6]
ss = Solution()
print(ss.hIndex(citations=citations))

