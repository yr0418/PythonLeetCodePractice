# -*- coding: utf-8 -*-
# @File : solution.py
# @Description：算法
# @Author : 杨睿
# @Time : 2021-01-14 23:21
from typing import *


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
        result = 0
        while x != 0:
            pop = x % 10
            x = x / 10
            result = result * 10 + pop
            if -pow(2, 31) <= result <= pow(2, 31) - 1:
                continue
            else:
                return 0
        return result
