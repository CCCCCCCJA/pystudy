class Solution(object):
    def pairSums(self, nums, target):
        tmp = []
        res = []
        tmp.append(nums[0])
        for i in range(1, len(nums)):
            tmpn = target - nums[i]
            if tmpn in tmp:
                res.append([tmpn, nums[i]])
                tmp.remove(tmpn)
            else:
                tmp.append(nums[i])
        print(res)
        return res
