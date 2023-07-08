# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        # 148ms
        def traversal(inorder, postorder):
            if len(postorder) == 0:
                return None
            rootvalue = postorder[-1]
            root = TreeNode(rootvalue)
            if len(postorder) == 1:
                return root
            indexi = inorder.index(rootvalue)
            indexp = postorder.index(rootvalue)
            leftinorder = inorder[:indexi]
            rightinorder = inorder[indexi+1:]
            leftpostorder = postorder[:len(leftinorder)]
            rightpostorder = postorder[len(leftinorder):len(rightinorder)+len(leftinorder)]
            root.left = traversal(leftinorder, leftpostorder)
            root.right = traversal(rightinorder, rightpostorder)
            return root