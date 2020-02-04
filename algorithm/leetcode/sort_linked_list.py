#!/usr/bin/env python
# coding=utf-8

"""
题目：
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 要求O(nlogn)的时间复杂度和常数级别的空间复杂度
解法：
   根据时间复杂度的要求，满足条件的有：快速排序、归并排序。对数组做归并排序的时间复杂度为O(n)，分别由开辟新数组O(n)和递归调用O(logn)。
   因此，为满足条件不能使用递归调用。这里为方便理解归并排序，将递归调用的解法也写在这里。
   1) 递归解法：
      1. 切分链表：使用快慢指针找到链表中点  2. 递归调用切分  3. 合并两个链表

"""
class ListNode():
    def __init__(self, value):
        self.val = value
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        """
        递归
        :param head:
        :return:
        """
        if not head or not head.next:
            return head

        mid = self.cut_mid(head)
        return self.merge(self.sortList(head), self.sortList(mid))

    def merge(self, left: ListNode, right: ListNode) -> ListNode:
        """
        合并两个链表
        :param left:
        :param right:
        :return:
        """
        head = ListNode(0)
        p = head
        while left and right:
            if left.val < right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next

            p = p.next
        if left:
            p.next = left
        if right:
            p.next = right

        return head.next

    def cut_mid(self, node: ListNode) -> ListNode:
        """
        从链表中间切分
        :param node:
        :return: 后半部分节点链表
        """
        if not node:
            return None

        fast, slow, new_head = node, node, node
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        # 保留中间节点的下一个节点，用于返回
        new_head = slow.next
        # 将链表在中间截断
        slow.next = None

        return new_head

