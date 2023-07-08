# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # 188ms
        def traversal(nums):
            if len(nums) == 0:
                return None
            max_num = max(nums)
            root = TreeNode(max_num)
            if len(nums) == 1:
                return root
            ids_num = nums.index(max_num)
            root.left = traversal(nums[:ids_num])
            root.right = traversal(nums[ids_num+1:])
            return root
        return traversal(nums)
        # 单调栈解法更优

nums = [3,2,1,6,0,5]
ss = Solution()
ss.constructMaximumBinaryTree(nums)