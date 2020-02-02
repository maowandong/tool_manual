#!/usr/bin/env python
# coding=utf-8

"""
题目：
    LRU cache实现
解法：
    双向链表 +  map
"""

class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None

class LRUCache():
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.cache = {}
        self.head, self.tail = DLinkedNode(), DLinkedNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node):
        '''
        增加节点
        :param node:
        :return:
        '''

        # 先处理当前节点的前后关系（新节点的前后关系为空，）
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        '''
        去除一个节点
        :param node:
        :return:
        '''

        # 前节点的后一节点为当前节点的后节点
        # 后一节点的前节点为当前节点的前节点
        node.prev.next = node.next
        node.next.prev = node.prev

    def _move_to_head(self, node):
        '''
        将节点移动到最热位置，表头
        :param node:
        :return:
        '''
        self._remove_node(node)
        self._add_node(node)

    def _pop_tail(self):
        '''
        弹出表尾
        :return:
        '''
        tail = self.tail.prev
        self._remove_node(tail)

        return tail

    def get(self, key):
        '''
        获取元素
        :param key:
        :return:
        '''
        node = self.cache.get(key, None)
        if not node:
            return -1

        self._move_to_head(node)

        return node.value

    def put(self, key, value):
        '''
        添加元素
        :param key:
        :param value:
        :return:
        '''
        node = self.cache.get(key, None)
        if not node:
            new_node = DLinkedNode()
            new_node.key = key
            new_node.value = value
            new_node.prev = DLinkedNode()
            new_node.next = DLinkedNode()

            self.cache[key] = new_node
            self._add_node(new_node)
            self.size += 1

            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1
        else:
            node.value = value
            self._move_to_head(node)

cache = LRUCache(2)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(1,5)

print(cache.get(2))