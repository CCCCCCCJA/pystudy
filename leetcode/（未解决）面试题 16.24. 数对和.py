class Solution(object):
    def pairSums(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        tmpNums = nums.copy()
        for i in range(len(nums) // 2 + 1):
            for j in range(len(tmpNums)):
               tmpTar = target - tmpNums[j]
               if tmpTar in tmpNums:

                   indexTar = tmpNums.index(tmpTar)
                   if j == indexTar: continue
                   res.append([tmpNums[j], tmpTar])
                   tmpNums.pop(j)
                   tmpNums.pop(indexTar-1)
                   break
        print(res)
        return res

nums = [-2,-1,0,3,5,6,7,9,13,14]
target = 12
ss = Solution()
ss.pairSums(nums, target)


