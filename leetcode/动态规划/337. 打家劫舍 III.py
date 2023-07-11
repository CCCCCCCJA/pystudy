# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 树形DP
        # dp[0]不偷的最大金额
        # dp[1]偷的最大金额
        # carl 16ms 100%
        def dfs(node):
            if node is None:
                return [0, 0]
            leftdp = dfs(node.left)
            rightdp = dfs(node.right)
            val0 = max(leftdp) + max(rightdp)
            val1 = node.val + leftdp[0] + rightdp[0]
            return [val0, val1]
        return max(dfs(root))
