"""
-*- coding: utf-8 -*-
@file : solution.py
@description：
@author : 杨睿
@time : 2022-01-06 15:11
"""
from typing import Optional

from Tree import TreeNode


class Solution:
    def tree2str_1(self, root: Optional[TreeNode]) -> str:
        """
        根据二叉树创建字符串
        """
        if not root:
            return ''
        left = '(' + self.tree2str(root.left) + ')' if (root.left or root.right) else ''
        right = '(' + self.tree2str(root.right) + ')' if root.right else ''
        return str(root.val) + left + right

    def tree2str_2(self, t: TreeNode) -> str:
        """
        根据二叉树创建字符串
        """
        def preorder(root):
            if not root:
                return ''
            if not root.left and root.right:  # 左边为空右边不为空的时需要加一个空括号保证映射关系
                return str(root.val) + '()' + '(' + preorder(root.right) + ')'
            if root.left and not root.right:
                return str(root.val) + '(' + preorder(root.left) + ')'
            if not root.left and not root.right:
                return str(root.val)
            return str(root.val) + '(' + preorder(root.left) + ')' + '(' + preorder(root.right) + ')'

        return preorder(t)

    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        """
        合并二叉树
        """
        if not root1:
            return root2
        if not root2:
            return root1

        merged = TreeNode(root1.val + root2.val)
        merged.left = self.mergeTrees(root1.left, root2.left)
        merged.right = self.mergeTree(root1.right, root2.right)
        return merged







