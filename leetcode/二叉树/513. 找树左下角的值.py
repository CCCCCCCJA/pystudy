# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历40ms
        # carl 20ms
        self.maxdepth = float('-inf')
        self.res = 0
        def traversol(node, depth):
            if node.left is None and node.right is None:
                if depth > self.maxdepth:
                    self.maxdepth = depth
                    self.res = node.val
                return
            if node.left:
                traversol(node.left, depth + 1)
            if node.right:
                traversol(node.right, depth + 1)
        traversol(root, 0)
        return self.res

