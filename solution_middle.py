"""
-*- coding: utf-8 -*-
@file : solution_middle.py
@description：中等算法
@author : 杨睿
@time : 2021-02-14 10:07
"""
from typing import *


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        :description: 移除重复字母
        :param s: str
        :return: str
        """
        # 计算每个字母在s中出现的次数，记录在cha_dict中：
        cha_dict = {}
        for cha in s:
            if cha not in cha_dict :
                cha_dict[cha] = 0
            cha_dict[cha] += 1

        # 建立一个栈tmp,保持栈是字典序最小：
        tmp = ['0']  # 为了防止出现tmp[-1]报错，左边加入最小哨兵
        for cha in s:  # 遍历字符串
            if cha not in tmp:  # 如果当前字符如果不在栈中，需要把它安排在合适的位置。
                while cha < tmp[-1]:
                    if cha_dict[tmp[-1]] > 0:  # 当栈顶元素比当前字符大，且之后还会出现，则将其删除
                        del tmp[-1]
                    else:  # 当栈顶元素不会再出现时，停止
                        break
                tmp.append(cha)
            # 如果当前字符如果已经在栈中，则它已经是在目前的最优位置了，不需要进行处理。
            cha_dict[cha] -= 1  # 当前元素的剩余数量-1
        ans = ''.join(tmp[1:])
        return ans
