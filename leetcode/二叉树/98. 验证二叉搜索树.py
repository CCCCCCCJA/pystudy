# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # 40ms
        # self.max_nums = float('-inf')
        # def valib(root):
        #     if root is None:
        #         return True
        #     leftvalid = valib(root.left)
        #     if root.val > self.max_nums:
        #         self.max_nums = root.val
        #     else:
        #         return False
        #     rightvalib = valib(root.right)
        #     return leftvalid and rightvalib
        # return valib(root)
        self.pre = None
        def valib(root):
            if root is None:
                return True
            leftvalid = valib(root.left)
            if self.pre and self.pre.val > root.val:
                return False
            else:
                self.pre = root
            rightvalib = valib(root.right)
            return leftvalid and rightvalib
        return valib(root)

