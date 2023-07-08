# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        # res = []
        # def dfs(root):
        #     if not root:
        #         return
        #     dfs(root.left)
        #     res.append(root.val)
        #     dfs(root.right)
        # dfs(root)
        # return res
        # 迭代
        res = []
        st = []
        cur = root
        while cur is not None or len(st) != 0:
            if cur is not None:
                st.append(cur)
                cur = cur.left
            else:
                cur = st.pop()
                res.append(cur.val)
                cur = cur.right
        return res


root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
ss = Solution()
print(ss.inorderTraversal(root))