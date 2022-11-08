class Solution(object):
    def longestConsecutive(self, nums):
        # 执行时间：44ms
        setn = set(nums)
        listn = list(setn)
        listn.sort()
        count = 1
        res = []
        if len(nums) == 0:
            return 0
        for i in range(len(listn)-1):
            if listn[i] + 1 == listn[i+1]:
                count += 1
            else:
                res.append(count)
                count = 1
        res.append(count)
        # print(max(res))
        return max(res)

nums = [1,0,-1]
ss = Solution()
print(ss.longestConsecutive(nums))