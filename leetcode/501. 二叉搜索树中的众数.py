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
        res = []
        def dfs(root):
            if not root:
                return
            # 按照 左-打印-右的方式遍历
            dfs(root.left)
            res.append(root.val)
            dfs(root.right)
        dfs(root)
        set_res = set(res)
        count = []
        list_res = list(set_res)
        for sr in set_res:
            tmpcount = res.count(sr)
            count.append(tmpcount)
        print(count)
        k = count.count(max(count))
        resres = []
        for i in range(k):
            maxcount = max(count)
            indexmax = count.index(maxcount)
            resres.append(list_res[indexmax])
            count[indexmax] = -1
        print(resres)
        return resres

root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(2)
ss = Solution()
print(ss.findMode(root))
