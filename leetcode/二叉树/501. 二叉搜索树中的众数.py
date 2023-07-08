# Definition for a binary tree node.
# 没有使用到二叉搜索树的相关性质
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.pre = None
        self.count = 0
        self.maxCount = 0
        res = []
        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            if self.pre == None:
                self.count = 1
            elif self.pre.val == root.val:
                self.count += 1
            else:
                self.count = 1
            self.pre = root
            if self.count == self.maxCount:
                res.append(root.val)
            if self.count > self.maxCount:
                self.maxCount = self.count
                res.clear()
                res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
ss = Solution()
print(ss.findMode(root))
