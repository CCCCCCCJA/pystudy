class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        res = [0]
        for gg in gain:
            print(res[-1])
            res.append(res[-1] + gg)
        print(res)
        return max(res)


gain = [-5, 1, 5, 0, -7]
ss = Solution()
ss.largestAltitude(gain)