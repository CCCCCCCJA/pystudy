# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        # 28ms
        def dfs(root, low, high):
            if not root:
                return None
            if root.val < low:
                return dfs(root.right, low, high)
            if root.val > high:
                return dfs(root.left, low, high)
            root.left = dfs(root.left, low, high)
            root.right = dfs(root.right, low, high)
            return root
        return dfs(root, low, high)