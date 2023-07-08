# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 层序方法 880ms
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
        #     if len(tmp) < 2 ** count:
        #         return (2 ** (count) - 1) + len(tmp)
        #     count += 1
        # if len(tmp) == 2 ** (count-1):
        #     return (2 ** count) - 1
        # 前序递归 128ms
        # res = []
        # def backing(root):
        #     if root == None:
        #         return
        #     res.append(root.val)
        #     backing(root.left)
        #     backing(root.right)
        # backing(root)
        # return len(res)
        # 前序迭代 84ms
        # count = 0
        # stack = [root]
        # while len(stack) != 0:
        #     tmp = stack.pop()
        #     if tmp is not None:
        #         count += 1
        #     else:
        #         continue
        #     stack.append(tmp.right)
        #     stack.append(tmp.left)
        # return count
        # cral
        def getNum(node):
            if node is None:
                return 0
            left = node.left
            right = node.right
            leftdepth = 0
            rightdepth = 0
            while left:
                left = left.left
                leftdepth += 1
            while right:
                right = right.right
                rightdepth += 1
            if leftdepth == rightdepth:
                return (2 ** leftdepth) - 1
            leftnum = getNum(node.left)
            right = getNum(node.right)
            return leftnum + right
        return getNum(root)