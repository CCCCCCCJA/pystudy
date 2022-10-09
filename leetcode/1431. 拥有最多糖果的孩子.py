class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        max_c = max(candies)
        res = []
        for c in candies:
            if (c + extraCandies) >= max_c :
                res.append(True)
            else:
                res.append(False)
        return res

candies = [2,3,5,1,3]
extraCandies = 3
ss = Solution()
print(ss.kidsWithCandies(candies, extraCandies))