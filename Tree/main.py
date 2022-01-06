
"""
-*- coding: utf-8 -*-
@file : main.py
@description：
@author : 杨睿
@time : 2022-01-06 16:53
"""
from Tree.TreeNode import TreeNode

if __name__ == '__main__':
    node1 = TreeNode(1)
    node1.insert(None)
    node1.insert(3)
    node1.insert(4)
    node1.print_tree()


