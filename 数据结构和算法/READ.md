1. 抽象数据类型和面向对象编程
2. 数组和列表
3. 单链表
4. 双链表



# ADT(抽象数据类型)

python直接运行

    python bag_adt.py

py.test测试框架运行

    py.test bag_adt.py

​    



# 数组和列表

线性结构

    内存连续
    下标访问


| 操作                                | 平均时间复杂度 |
| :---------------------------------- | :------------: |
| list[index]                         |      O(1)      |
| list.append                         |      O(1)      |
| list.insert                         |      O(n)      |
| list.pop(index),deault last element |      O(1)      |
| list.remove                         |      O(n)      |



线性：连续、下标访问

链式：不连续、无法下标访问



# 单链表

时间复杂度

| 操作                          | 平均时间复杂度 |
| ----------------------------- | :------------: |
| linked_list.append(value)     |      O(1)      |
| linked_list.appendleft(value) |      O(1)      |
| linked_list.find(value)       |      O(n)      |
| linked_list.remove(value)     |      O(n)      |



# 双链表

