# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getHeight(node):
            if node is None:
                return 0
            # 左
            leftHeight = getHeight(node.left)
            # 右
            rightHeight = getHeight(node.right)
            # 中
            if node.left is None and node.right is not None:
                return 1 + rightHeight
            elif node.left is not None and node.right is None:
                return 1 + leftHeight
            return 1 + min(leftHeight, rightHeight)
        res = getHeight(root)
        return res