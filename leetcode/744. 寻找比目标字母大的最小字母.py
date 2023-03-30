class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        left = 0
        right = len(letters) - 1
        while left < right:
            middle = int((left + right) / 2)
            if letters[middle] == target:
                return letters[middle + 1]
            elif letters[middle] > target:
                right = middle - 1
            else:
                left = middle + 1


letters = ["c","f","j"]
target = 'd'
ss = Solution()
print(ss.nextGreatestLetter(letters, target))