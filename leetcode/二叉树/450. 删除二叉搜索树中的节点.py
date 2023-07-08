# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # 89/92 未通过
        # pre = None
        # tmp = root
        # global tag
        # while tmp:
        #     tmpval = tmp.val
        #
        #     if tmp.val > key:
        #         pre = tmp
        #         tag = 0
        #         tmp = tmp.left
        #     elif tmp.val < key:
        #         pre = tmp
        #         tag = 1
        #         tmp = tmp.right
        #     else:
        #         if tmp.left is None and tmp.right is None:
        #             if not pre:
        #                 return None
        #             else:
        #                 if tag == 0:
        #                     pre.left = None
        #                 else:
        #                     pre.right = None
        #             return root
        #         elif tmp.left is not None and tmp.right is None:
        #             if not pre:
        #                 return tmp.left
        #             else:
        #                 if tag == 0:
        #                     pre.left = tmp.left
        #                 else:
        #                     pre.right = tmp.left
        #             return root
        #         elif tmp.left is None and tmp.right is not None:
        #             if not pre:
        #                 return tmp.right
        #             else:
        #                 if tag == 0:
        #                     pre.left = tmp.right
        #                 else:
        #                     pre.right = tmp.right
        #             return root
        #         else:
        #             cur = tmp
        #             pre = cur
        #             cur = cur.right
        #             flag = 0
        #             while cur.left:
        #                 flag = 1
        #                 pre = cur
        #                 cur = cur.left
        #             tmp.val = cur.val
        #             if flag:
        #                 pre.left = None
        #             else:
        #                 pre.right = pre.right.right
        #             return root
        # return root
        #carl 48ms
        def dfs(root, key):
            if root is None:
                return root
            if root.val == key:
                if root.left is None and root.right is None:
                    return None
                elif root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                else:
                    cur = root.right
                    while cur.left is not None:
                        cur = cur.left
                    cur.left = root.left
                    return root.right
            if root.val > key:
                root.left = dfs(root.left, key)
            if root.val < key:
                root.right = dfs(root.right, key)
            return root
        return dfs(root, key)
