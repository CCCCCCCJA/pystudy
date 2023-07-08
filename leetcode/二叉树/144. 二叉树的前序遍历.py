# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # res = []
        # def backing(root):
        #     if root == None:
        #         return
        #     res.append(root.val)
        #     backing(root.left)
        #     backing(root.right)
        # backing(root)
        # return res
        res = []
        stack = [root]
        while len(stack) != 0:
            tmp = stack.pop()
            if tmp is not None:
                res.append(tmp.val)
            else:
                continue
            stack.append(tmp.right)
            stack.append(tmp.left)
        return res

