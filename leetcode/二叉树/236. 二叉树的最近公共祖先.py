# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 不怎么理解
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 48ms
        def dfs(node, p, q):
            if not node:
                return None
            if node is p or node is q:
                return node
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if left is not None and right is not None:
                return node
            if left is not None and right is None:
                return left
            if left is None and right is not None:
                return right
            if left is None and right is None:
                return None
        return dfs(root, p, q)
