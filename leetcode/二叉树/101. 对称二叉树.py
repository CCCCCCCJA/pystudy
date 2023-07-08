# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def compare(left, right):
            if left == None and right != None:
                return False
            elif left != None and right == None:
                return False
            elif left == None and right == None:
                return True
            # 排除了空节点，再排除数值不相同的情况
            elif left.val != right.val:
                return False

            outside = compare(left.left, right.right)
            inside = compare(left.right, right.left)
            return outside and inside
        return compare(root.left, root.right)



root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(3)
root.right.right = TreeNode(4)
ss = Solution()
print(ss.isSymmetric(root))