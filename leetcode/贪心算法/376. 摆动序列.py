class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 卡尔   20ms
        # if len(nums) == 1:
        #     return 1
        # if len(nums) == 2:
        #     if nums[0] == nums[1]:
        #         return 1
        #     else:
        #         return 2
        # prediff = 0
        # curdiff = 0
        # res = 1
        # for i in range(len(nums)-1):
        #     curdiff = nums[i+1] - nums[i]
        #     if (prediff >= 0 and curdiff < 0) or (prediff <= 0 and curdiff > 0):
        #         res += 1
        #         prediff = curdiff
        # # print(res)
        # return res
        # 自己写的    12 ms
        if len(nums) == 1:
            return 1
        if len(nums) == 2:
            if nums[0] == nums[1]:
                return 1
            else:
                return 2
        if nums[0] != nums[1]:
            res = 2
        else:
            res = 1
        diff = []
        for i in range(1, len(nums)):
            diff.append(nums[i] - nums[i-1])
        print(diff)
        if diff[0] < 0:
            tag = 0
        elif diff[0] > 0:
            tag = 1
        else:
            flag = 1
        for i in range(1, len(diff)):
            if flag == 1:
                if diff[i] > 0:
                    tag = 1
                    res += 1
                    flag = 0
                    continue
                elif diff[i] < 0:
                    tag = 0
                    res += 1
                    flag = 0
                    continue
                else:
                    continue
            if tag == 0 and diff[i] > 0:
                tag = 1
                res += 1
            elif tag == 1 and diff[i] < 0:
                tag = 0
                res += 1
            else:
                continue
        print(res)
        return res



nums = [1,1,7,4,9,2,5]
# nums = [3,3,3,4,3]
ss = Solution()
ss.wiggleMaxLength(nums)