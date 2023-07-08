# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 52ms
        # res = []
        # def getres(root):
        #     if root is None:
        #         return
        #     getres(root.left)
        #     res.append(root.val)
        #     getres(root.right)
        # getres(root)
        # minchazhi = float('inf')
        # for i in range(len(res)-1):
        #     if abs(res[i]-res[i+1]) > minchazhi:
        #         minchazhi = abs(res[i]-res[i+1])
        # return minchazhi
        # 40ms
        self.pre = None
        self.minchazhi = 10 ** 5 + 1
        def valib(root):
            if root is None:
                return
            valib(root.left)
            if self.pre is not None:
                if abs(self.pre.val - root.val) < self.minchazhi:
                    self.minchazhi = abs(self.pre.val - root.val)
            self.pre = root
            valib(root.right)
        return self.minchazhi


root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
ss = Solution()
ss.getMinimumDifference(root)
