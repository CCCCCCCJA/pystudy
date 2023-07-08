# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # 20ms
        path = []
        res = []
        def tacking(node):
            path.append(node.val)
            if node.left is None and node.right is None:
                tmp = ''
                for i in range(len(path)-1):
                    tmp += str(path[i]) + '->'
                tmp += str(path[-1])
                res.append(tmp)
                return
            if node.left:
                tacking(node.left)
                path.pop()
            if node.right:
                tacking(node.right)
                path.pop()
        tacking(root)
        # print(res)
        return res