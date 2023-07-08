# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 56ms
    #     res = []
    #     def backing(root):
    #         if root == None:
    #             return
    #         leftdeepth = self.getHeight(root.left)
    #         rightdeepth = self.getHeight(root.right)
    #         if abs(leftdeepth-rightdeepth) > 1:
    #             res.append(1)
    #             return
    #         else:
    #             backing(root.left)
    #             backing(root.right)
    #     backing(root)
    #     if len(res) == 0:
    #         return True
    #     else:
    #         return False
    #
    # def getHeight(self, node):
    #     if node is None:
    #         return 0
    #     # 左
    #     leftHeight = self.getHeight(node.left)
    #     # 右
    #     rightHeight = self.getHeight(node.right)
    #     # 中
    #     return 1 + max(leftHeight, rightHeight)
        # carl 24ms
        def getHeight(node):
            if node is None:
                return 0
            leftheight = getHeight(node.left)
            if leftheight == -1:
                return -1
            rightheight = getHeight(node.right)
            if rightheight == -1:
                return -1
            res = 0
            if abs(leftheight-rightheight) > 1:
                res = -1
            else:
                res = 1 + max(leftheight, rightheight)
            return res

        return getHeight(root)