class Solution(object):
    def findArray(self, pref):
        """
        :type pref: List[int]
        :rtype: List[int]
        """
        arr = []
        tag = 0
        for pf in pref:
            res = pf
            if tag == 0:
                arr.append(pf)
                tag += 1
                continue
            for a in arr:
                res ^= a
            arr.append(res)
        print(arr)
        return arr


pref = [5, 2, 0, 3, 1]
ss = Solution()
ss.findArray(pref)
