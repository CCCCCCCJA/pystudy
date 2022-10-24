# Definition for a binary tree node.
# 时间空间复杂度都太高    也没有用到二叉搜索树的一些性质
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    res = []
    def minDiffInBST(self, root):
        self.minmin(root)
        print(self.res)
        tmp = []
        for i in range(len(self.res)-1):
            for j in range(i+1, len(self.res)):
                if self.res[i] - self.res[j] > 0:
                    tmp.append(self.res[i] - self.res[j])
                else:
                    tmp.append(self.res[j] - self.res[i])
        print(min(tmp))
        return min(tmp)
    def minmin(self, root):
        if root == None:
            return
        self.res.append(root.val)
        self.minmin(root.left)
        self.minmin(root.right)


root = TreeNode(0)
root.val = 27
root.left = None
root.right = TreeNode(val=34)
root.right.right = TreeNode(val=58)
root.right.right.left = TreeNode(val=50)
root.right.right.left.left = TreeNode(val=44)
ss = Solution()
print(ss.minDiffInBST(root))