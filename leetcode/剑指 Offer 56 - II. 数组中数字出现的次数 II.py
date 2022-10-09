# 内存  用时都高

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []
        tag = []
        for n in nums:
            if (n not in temp) & (n not in tag):
                temp.append(n)
            elif n in tag:
                continue
            else:
                tag.append(n)
                temp.remove(n)
        print(tag)
        print(temp)
        return temp[0]

nums = [9,1,7,9,7,9,7]
ss = Solution()
print(ss.singleNumber(nums))