class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        global start
        tag = 0
        res = []
        for i in range(len(nums)):
            if tag == 0:
                start = nums[i]
                tag = 1
            if i == len(nums)-1:
                if nums[i] == nums[i-1] + 1:
                    end = nums[i]
                    res.append(str(start) + '->' + str(end))
                else:
                    res.append(str(nums[i]))
                break
            if nums[i] + 1 == (nums[i+1]):
                continue

            else:
                end = nums[i]
                if end == start:
                    res.append(str(start))
                    tag = 0
                else:
                    res.append(str(start) + '->' + str(end))
                    tag = 0
        # print(res)
        return res

nums = [0,2,3,4,6,8,9]
ss = Solution()
ss.summaryRanges(nums)
