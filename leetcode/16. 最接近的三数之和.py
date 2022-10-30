class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 时间复杂度n**3
        # 超时
        # sum = []
        # res = []
        # lenlen = len(nums)
        # for i in range(lenlen-2):
        #     for j in range(i+1, lenlen-1):
        #         for k in range(j+1, lenlen):
        #             sum.append(nums[i] + nums[j] + nums[k])
        # for i in range(len(sum)):
        #     res.append(abs(sum[i]-target))
        # print(sum)
        # print(res)
        # indexres = res.index(min(res))
        # return sum[indexres]
        nums.sort()
        best = 10 ** 7
        def updata(cur):
            nonlocal best
            if abs(cur - target) < abs(best - target):
                best = cur
        for i in range(len(nums)):
            k = i+1
            m = len(nums)-1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while k < m:
                ss = nums[i] + nums[k] + nums[m]
                if ss == target:
                    return ss
                updata(ss)
                if ss > target:
                    m0 = m - 1
                    while nums[m] == nums[m0] and m0 > k:
                        m0 -= 1
                    m = m0
                else:
                    k0 = k + 1
                    while nums[k] == nums[k0] and k0 < m:
                        k0 += 1
                    k = k0
        return best

nums = [0,0,0]
target = 1
ss = Solution()
print(ss.threeSumClosest(nums, target))