# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        res = []
        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ss = Solution()
print(ss.inorderTraversal(root))