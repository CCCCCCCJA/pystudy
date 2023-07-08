# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序遍历方法
        # if root is not None:
        #     queue = [root]
        # else:
        #     return []
        # count = 0
        # while len(queue) != 0:
        #     lenq = len(queue)
        #     tmp = []
        #     for i in range(lenq):
        #         node = queue.pop(0)
        #         tmp.append(node.val)
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     count += 1
        # return count
        # 后序遍历方法    求高度
        def getHeight(node):
            if node is None:
                return 0
            # 左
            leftHeight = getHeight(node.left)
            # 右
            rightHeight = getHeight(node.right)
            # 中
            return 1 + max(leftHeight, rightHeight)
        res = getHeight(root)
        return res


root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
ss = Solution()
ss.maxDepth(root)