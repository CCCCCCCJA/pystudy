class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i, j]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1



numbers = [0,0,3,4]
target = 0
ss = Solution()
print(ss.twoSum(numbers, target))