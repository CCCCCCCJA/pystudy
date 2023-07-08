# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 48ms 90%
        def dfs(node, p, q):
            if not node:
                return None
            if node is p or node is q:
                return node
            tmp = node.val
            if node.val < p.val and node.val < q.val:
                return dfs(node.right, p, q)
            elif node.val > p.val and node.val > q.val:
                return dfs(node.left, p, q)
            else:
                return node
        return dfs(root, p, q)


root = TreeNode(6)
root.left = TreeNode(2)
root.right = TreeNode(8)
root.left.left = TreeNode(0)
root.left.right = TreeNode(4)
root.right.left = TreeNode(7)
root.right.right = TreeNode(9)
root.left.right.left = TreeNode(3)
root.left.right.right = TreeNode(5)
p = root.left.right.left
q = root.left.right.right
ss = Solution()
ss.lowestCommonAncestor(root,p, q)


