# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        # myself 24ms
        self.valsum = 0
        self.res = False
        def getTarget(node, targetSum):
            # tmp1 = node.val
            self.valsum += node.val
            # tmp2 = self.valsum
            if self.res is True:
                return
            if node.left is None and node.right is None:
                if self.valsum == targetSum:
                    self.res = True
                self.valsum -= node.val
                return
            if node.left:
                getTarget(node.left, targetSum)
            if node.right:
                getTarget(node.right, targetSum)
            self.valsum -= node.val
        if root is None:
            return False
        getTarget(root, targetSum)
        return self.res


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
ss = Solution()
print(ss.hasPathSum(root, 22))