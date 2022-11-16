class Solution(object):
    def divisorSubstrings(self, num, k):
        strnum = str(num)
        count = 0
        for i in range(len(strnum)-k+1):
            tmp = int(strnum[i:i+k])
            if tmp == 0:
                continue
            if num // tmp == num / tmp:
                count += 1
        print(count)
        return count

num = 240
k = 2
ss = Solution()
ss.divisorSubstrings(num, k)