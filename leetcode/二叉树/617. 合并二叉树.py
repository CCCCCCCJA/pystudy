# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 52ms
        # def abc(root1, root2):
        #     if root1 is None and root2 is None:
        #         return None
        #     if root1 is not None and root2 is None:
        #         root = TreeNode(root1.val)
        #         root.left = root1.left
        #         root.right = root1.right
        #         return root
        #     if root1 is None and root2 is not None:
        #         root = TreeNode(root2.val)
        #         root.left = root2.left
        #         root.right = root2.right
        #         return root
        #     root = TreeNode(root1.val + root2.val)
        #     root.left = abc(root1.left, root2.left)
        #     root.right = abc(root1.right, root2.right)
        #     return root
        # return abc(root1, root2)
        # carl 56ms
        def merge(root1, root2):
            if root1 is None:
                return root2
            if root2 is None:
                return root1
            root1.val += root2.val
            root1.left = merge(root1.left, root2.left)
            root1.right = merge(root1.right, root2.right)
            return root1
        return merge(root1, root2)
            

root1 = TreeNode(1)
root1.left = TreeNode(2)
root1.left = TreeNode(3)
root2 = TreeNode(1)
root2.right = TreeNode(2)
root2.right = TreeNode(3)
ss = Solution()
ss.mergeTrees(root1, root2)
