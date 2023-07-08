# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        # 64ms 30%
        self.pre = None
        def dfs(root):
            if not root:
                return 0
            dfs(root.right)
            if not self.pre:
                root.val += self.pre.val
            self.pre = root
            dfs(root.left)
            return root.val
        dfs(root)
        return root
