class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """
        lenorg = len(original)
        if n * m != lenorg:
            return []
        res = []
        tmp = []
        for i in range(m):
            for j in range(n):
                tmp.append(original[j])
            original = original[n:]
            res.append(tmp)
            tmp = []
        print(res)
        return res

original = [1,2,3]
m = 1
n = 3
ss = Solution()
ss.construct2DArray(original, m, n)