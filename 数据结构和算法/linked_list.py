# -*- coding:utf-8 -*-
# /usr/bin/env python

"""
Author:zhengpanone
Email:zhengpanone@hotmail.com
date:2019/8/26 18:32

单链表
"""


# import lib
class Node:
    def __init__(self, value=None, next=None):
        self.value, self.next = value, next


class LinkedList:
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tail_node = None

    def __len__(self):
        return self.length

    def append(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception("Full")
        node = Node(value)
        tail_node = self.tail_node
        if tail_node is None:
            self.root.next = node
        else:
            tail_node.next = node
        self.tail_node = node
        self.length += 1

    def append_left(self, value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length += 1

    def iter_node(self):
        """
        遍历从head 节点到tail节点
        :return:
        """
        cur_node = self.root.next
        while cur_node is not self.tail_node:  # 从第一个节点开始遍历
            yield cur_node
            cur_node = cur_node.next  # 移动到下一个节点
        yield cur_node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def remove(self, value):  # O(n)
        """
        删除包含值的一个节点，将其从前一个节点的next指向被查询节点的的下一个即可
        :param value:
        :return:
        """
        prev_node = self.root
        cur_node = self.root.next
        for cur_node in self.iter_node():
            if cur_node.value == value:  # 注意更新tail_node
                prev_node.next = cur_node.next
                if cur_node is self.tail_node:
                    self.tail_node = prev_node
                del cur_node
                self.length -= 1
                return 1  # 表示删除成功
            else:
                prev_node = cur_node  # 更新prev_node
            return -1  # 表明删除失败

    def find(self, value):  # O(n)
        """
        查找一个节点,返回序号，从0开始
        :param value:
        :return:
        """
        index = 0
        for node in self.iter_node():  # 定义了__iter__ ，可以使用for遍历
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):  # O(1)
        if self.root.next is None:
            raise Exception('pop from empty LinkedList')
        head_node = self.root.next
        self.root.next = head_node.next
        self.length -= 1
        value = head_node.value
        del head_node
        return value

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next = None
        self.length = 0


def test_linked_list():
    ll = LinkedList()
    ll.append(0)
    ll.append(1)
    ll.append(2)

    assert len(ll) == 3
    assert ll.find(2) == 2
    assert ll.find(3) == -1

    ll.remove(0)
    assert len(ll) == 2
    assert ll.find(0) == -1

    assert list(ll) == [1, 2]

    ll.append_left(0)
    assert list(ll) == [0, 1, 2]
    assert len(ll) == 3

    head_value = ll.popleft()
    assert head_value == 0
    assert len(ll) == 2
    assert list(ll) == [1, 2]

    ll.clear()
    assert len(ll) == 0
