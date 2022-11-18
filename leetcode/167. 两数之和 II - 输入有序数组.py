class Solution(object):
    def twoSum(self, numbers, target):
        # 执行用时：24ms, 在所有Python提交中击败了78.73 %的用户
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [numbers[i], numbers[j]]
            elif numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
