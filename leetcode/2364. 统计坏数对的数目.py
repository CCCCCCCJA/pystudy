from collections import Counter


class Solution(object):
    def countBadPairs(self, nums):
        # 超时
        # lenlen = len(nums)
        # count = 0
        # for i in range(lenlen-1):
        #     for j in range(i+1, lenlen):
        #         # print(nums[i], nums[j])
        #         if j - i != nums[j] - nums[i]:
        #             count += 1
        # print(count)
        # return cou
        n, cnt = len(nums), Counter()
        ans = n * (n - 1) // 2
        for i, num in enumerate(nums):
            ans -= cnt[num - i]  # 有 cnt[num - i] 个相同的
            cnt[num - i] += 1
        return ans

nums = [4,1,3,3]
ss = Solution()
ss.countBadPairs(nums)