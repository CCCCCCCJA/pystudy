# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 16ms
        # count = []
        # def backing(node, tag):
        #     if node.left is None and node.right is None and tag == 1:
        #         count.append(node.val)
        #         return
        #     if node.left:
        #         backing(node.left, 1)
        #     if node.right:
        #         backing(node.right, 0)
        # backing(root, 0)
        # # print(count)
        # return sum(count)
        # carl 20ms
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 0
        tmp = root.val
        leftNum = self.sumOfLeftLeaves(root.left)
        if root.left is not None and root.left.left is None and root.left.right is None:
            leftNum = root.left.val
        rightNum = self.sumOfLeftLeaves(root.right)
        sum = leftNum + rightNum
        return sum

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ss = Solution()
print(ss.sumOfLeftLeaves(root))