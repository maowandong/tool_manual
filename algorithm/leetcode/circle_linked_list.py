#!/usr/bin/env python
# coding=utf-8

"""
题目：
    给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
解法：
   1) 遍历链表，存储访问过的节点，返回第一个被二次遍历到的节点即为入环的第一个节点
      时间复杂度O(n)， 空间复杂度O(n)
   2) 通过快慢指针是否相遇判断是否有环，相遇点有如下特性
      慢指针走距离： F(入环前距离) + a (环上距离)
      快指针走距离： F + a + b + a

      F + a + b + a = 2 * (F + a) =>  b = F， 即相遇点再往前走的距离和表头走到入环点的距离相等
"""


class Solution:
    def detectCycle_m1(self, head: ListNode) -> ListNode:
        """
        使用列表存储遍历过后的节点
        :param head:
        :return:
        """
        visited_node = []

        node = head
        while node:
            if node in visited_node:
                return node
            else:
                visited_node.append(node)

            node = node.next

        return None

    def detectCycle_m2(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        intersect = None
        while fast and slow:
            if not fast.next:
                break
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                intersect = fast
                break

        if not intersect:
            return None

        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1