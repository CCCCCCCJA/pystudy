# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        # 104ms 50%
        if not root:
            return TreeNode(val)
        tmp = root
        while tmp:
            if tmp.val > val:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left = TreeNode(val)
                    return root
            else:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    return root


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
ss = Solution()
ss.insertIntoBST(root, 5)