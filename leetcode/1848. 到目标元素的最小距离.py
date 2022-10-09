class Solution(object):
    def getMinDistance(self, nums, target, start):
        list = []
        indexs = []
        for i in range(len(nums)):
            if(nums[i] == target):
                indexs.append(i)
        for index in indexs:
            res1 = abs(index - start)
            list.append(res1)
        res = min(list)
        return res

nums = [1,2,3,4,5]
target = 5
start = 3
ss = Solution()
print(ss.getMinDistance(nums, target, start))