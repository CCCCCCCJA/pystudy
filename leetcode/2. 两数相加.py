# 代码超时！！！！！！！！！！！！！！！！！！！！！！！

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         p = l1
#         q = l2
#         x = l1
#         y = l2
#         tag = 0
#         cont = 0
#         while (p != None) | (q != None):
#             sum = p.val + q.val + tag
#             if sum >= 10:
#                 p.val = sum % 10
#                 tag = 1
#             else:
#                 p.val = sum
#             p = p.next
#             q = q.next
#             if cont > 0:
#                 x = x.next
#                 y = y.next
#             cont += 1
#         if (p == None) & (q != None):
#             if tag == 0:
#                 x.next = q
#                 return l1
#             else:
#                 x.next = q
#                 x = x.next
#                 while x != None:
#                     sum = x.val + tag
#                     if sum >= 10:
#                         x.val = sum % 10
#                         tag = 1
#                     else:
#                         x.val = sum
#                         break
#         if (q == None) & (p != None):
#             if tag == 0:
#                 return l1
#             else:
#                 while x != None
#                     sum = p.val + tag
#                     if sum >= 10:
#                         x.val = sum % 10
#                         tag = 1
#                     else:
#                         x.val = sum
#                         break
#         return l1

class Solution:
    def addTwoNumbers(self, l1, l2):

        # 定义头节点，val赋值为0
        head_node = ListNode(0)
        node = head_node

        # 进位标识符carry，初值为0
        carry = 0

        # while循环，对两链表对应位和上一位产生的进位carry进行相加操作，并判断是否产生了进位，记录carry值
        while l1 !=None or l2 != None:
            l1_num = l1.val if l1 != None else 0
            l2_num = l2.val if l2 != None else 0
            num = (l1_num + l2_num + carry)%10
            carry = 1 if l1_num + l2_num + carry>= 10 else 0  # 判断是否产生进位
            node.next = ListNode(num)  # 在链表尾部添加本次循环所得节点
            node = node.next
            l1 = l1.next if l1 !=None else None  # l1指向下一节点
            l2 = l2.next if l2 !=None else None  # l2指向下一节点

        # 循环后若最高位产生了进位则在链表尾部添加一个val为1的节点
        if carry == 1:
            node.next = ListNode(1)

        # 最后结果舍弃头节点
        head_node = head_node.next
        return head_node
