class Solution:
    def numPairsDivisibleBy60(self, time):
        cnt = [0] * 60
        for t in time:
            cnt[t % 60] += 1
        res = 0
        for i in range(1, 30):
            res += cnt[i] * cnt[60 - i]
        res += cnt[0] * (cnt[0] - 1) // 2 + cnt[30] * (cnt[30] - 1) // 2
        return res


time = [0,0,0]
ss = Solution()
print(ss.numPairsDivisibleBy60(time))
