# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def backing(root):
            if root is None:
                return root
            root.left, root.right = root.right, root.left
            backing(root.left)
            backing(root.right)
        backing(root)
        return root
