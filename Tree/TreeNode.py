"""
-*- coding: utf-8 -*-
@file : TreeNode.py
@description：
@author : 杨睿
@time : 2022-01-06 15:09
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val:
            if self.left is None:
                self.left = TreeNode(val)
            elif self.right is None:
                self.right = TreeNode(val)
            else:
                self.left.insert(val)
        else:
            self.val = val

    def print_tree(self):
        if self.val:
            print(self.val)
        if self.left:
            self.left.print_tree()
        if self.right:
            self.right.print_tree()

