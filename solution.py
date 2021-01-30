# -*- coding: utf-8 -*-
# @File : solution.py
# @Description：算法
# @Author : 杨睿
# @Time : 2021-01-14 23:21
from typing import *
import math


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :description：两数之和，暴力破解
        """
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        :description：两数之和，哈希表
        """
        hashtable = dict()
        for i, num in enumerate(nums):  # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
            if target - num in hashtable:  # key in dict：判断指定的键是否在字典中
                return [hashtable[target - num], i]
            hashtable[nums[i]] = i  # nums 中的数据进字典。nums[i] 为键，i为值
        return []

    def reverse(self, x: int) -> int:
        """
        :type x: int
        :rtype: int
        :description：整数反转
        """
        y, result = abs(x), 0  # 将 x 取绝对值，方便处理 负数，具体原因见 算法练习--2.3
        while y != 0:
            pop = y % 10
            y = y // 10  # 求余数，向下取整，单纯的 / 号，会使得 int 变成 float 类型
            result = result * 10 + pop
            #  边界的表示方法： boundry = (1<<31) -1 if x>0 else 1<<31。 result > boundry 即表示超过边界
            if -pow(2, 31) <= result <= pow(2, 31) - 1:
                continue
            else:
                return 0
        return result if x > 0 else -result

    def is_palindrome_1(self, x) -> bool:
        """
        :type x: int
        :rtype: bool
        :description: 回文数判断，借助字符串
        """
        # str(x)[::-1]：逆置截取全部字符，步长-1表示逆置截取字符串。
        return str(x) == str(x)[::-1]

    def is_palindrome_2(self, x) -> bool:
        """
        :type x: int
        :rtype: bool
        :description: 回文数判断，反转一半的数字
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10
