# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 48ms
        # self.res = False
        # self.resNode = None
        # def search(root, val):
        #     if self.res:
        #         return True
        #     if not root:
        #         return None
        #     if val == root.val:
        #         self.resNode = root
        #         self.res = True
        #     elif root.val > val:
        #         search(root.left, val)
        #     else:
        #         search(root.right, val)
        # search(root, val)
        # return self.resNode
        # carl 52ms 递归法
        # def search(root, val):
        #     if root is None or root.val == val:
        #         return root
        #     res = None
        #     if val < root.val:
        #         res = search(root.left, val)
        #     if val > root.val:
        #         res = search(root.right, val)
        #     return res
        #
        # return search(root, val)
        # 迭代法 52ms
        while root:
            if val == root.val:
                return root
            elif val > root.val:
                root = root.right
            else:
                root = root.left
        return None

