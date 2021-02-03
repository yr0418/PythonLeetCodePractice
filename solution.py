# -*- coding: utf-8 -*-
# @File : solution.py
# @Description：算法
# @Author : 杨睿
# @Time : 2021-01-14 23:21
from typing import *
from utils.ListNode import ListNode


class Solution:
    def twoSum_1(self, nums: List[int], target: int) -> List[int]:
        """
        description：两数之和，暴力破解
        """
        for index1 in range(len(nums)):
            for index2 in range(index1 + 1, len(nums)):
                if nums[index1] + nums[index2] == target:
                    return [index1, index2]

    def twoSum_2(self, nums: List[int], target: int) -> List[int]:
        """
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

    def is_palindrome_1(self, x: int) -> bool:
        """
        :description: 回文数判断，借助字符串
        """
        # str(x)[::-1]：逆置截取全部字符，步长-1表示逆置截取字符串。
        return str(x) == str(x)[::-1]

    def is_palindrome_2(self, x: int) -> bool:
        """
        :description: 回文数判断，反转一半的数字
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x //= 10
        return x == reverted_number or x == reverted_number // 10

    def romanToInt_1(self, s: str) -> int:
        """
        :description: 罗马数，暴力破解，字符串匹配
        """
        i, num = 0, 0
        while i < len(s):
            if s[i] == 'M':
                num = num + 1000
                i = i + 1
            elif s[i] == 'D':
                num = num + 500
                i = i + 1
            elif s[i] == 'C':
                if i == len(s) - 1:
                    num = num + 100
                    i = i + 1
                elif s[i + 1] == 'D':
                    num = num + 400
                    i = i + 2
                elif s[i + 1] == 'M':
                    num = num + 900
                    i = i + 2
                else:
                    num = num + 100
                    i = i + 1
            elif s[i] == 'L':
                num = num + 50
                i = i + 1
            elif s[i] == 'X':
                if i == len(s) - 1:
                    num = num + 10
                    i = i + 1
                elif s[i+1] == 'L':
                    num = num + 40
                    i = i + 2
                elif s[i+1] == 'C':
                    num = num + 90
                    i = i + 2
                else:
                    num = num + 10
                    i = i + 1
            elif s[i] == 'V':
                num = num + 5
                i = i + 1
            elif s[i] == 'I':
                if i == len(s)-1:
                    num = num + 1
                    i = i + 1
                elif s[i+1] == 'V':
                    num = num + 4
                    i = i + 2
                elif s[i+1] == 'X':
                    num = num + 9
                    i = i + 2
                else:
                    num = num + 1
                    i = i + 1
        return num

    def romanToInt_2(self, s: str) -> int:
        """
        :description: 罗马数，罗马数规律
        """
        prenum, num, sum = Solution.get_num(s[0]), 0, 0
        for i in range(1, len(s)):
            num = Solution.get_num(s[i])
            if prenum < num:
                sum = sum - prenum
            else:
                sum = sum + prenum
            prenum = num
        return sum + prenum

    @classmethod  # 加入 @classmethod 注释，方便直接调用该方法
    def get_num(cls, s: str) -> int:
        num = 0
        if s == 'M':
            num = 1000
        elif s == 'D':
            num = 500
        elif s == 'C':
            num = 100
        elif s == 'L':
            num = 50
        elif s == 'X':
            num = 10
        elif s == 'V':
            num = 5
        elif s == 'I':
            num = 1
        return num

    def romanToInt_3(self, s: str) -> int:
        """
        :description: 罗马数，罗马数规律，利用哈希表取值
        """
        roman_int = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int = 0
        for index in range(len(s)-1):
            if roman_int[s[index]] < roman_int[s[index+1]]:
                int -= roman_int[s[index]]
            else:
                int += roman_int[s[index]]
        return int + roman_int[s[-1]]

    def romanToInt_4(self, s: str) -> int:
        """
        :description: 罗马数，利用字典进行字符串匹配
        """
        # 注意在字典中 IX = 8，因为对于 XIX，第一次str1 = XI，匹配到 I，则 result+1，第二次匹配到 IX，则result + 8，两次合起来实现 IX = 9
        d = {'I': 1, 'IV': 3, 'V': 5, 'IX': 8, 'X': 10, 'XL': 30, 'L': 50, 'XC': 80, 'C': 100, 'CD': 300, 'D': 500, 'CM': 800, 'M': 1000}
        result = 0
        for i, n in enumerate(s):
            str1 = s[max(i - 1, 0):i + 1]  # 作者解析中的2就是用这行代码实现的
            if str1 in d:
                result += d.get(str1)
            else:
                result += d[n]
        return result

    def longestCommonPrefix_1(self, strs: List[str]) -> str:
        """
        :description: 最长公共前缀，字符串截取
        """
        if not strs:
            return ""
        else:
            str_1 = strs[0]
            for i in range(len(str_1)):
                for j in range(len(strs)):
                    # 正常情况
                    if strs[j][:i+1] != str_1[:i+1]:
                        return str_1[:i]
                    else:
                        continue
            # 解决异常情况，当strs里的值都是相同的时候
            return str_1

    def longestCommonPrefix_2(self, strs: List[str]) -> str:
        """
        :description: 最长公共前缀，字符串匹配，算法优化
        """
        if not strs:
            return ""
        # 利用 min 和 max 取 strs 中最长和最短的字符串
        str0 = min(strs)
        str1 = max(strs)
        for i in range(len(str0)):
            if str0[i] != str1[i]:
                return str0[:i]
        return str0

    def longestCommonPrefix_3(self, strs: List[str]) -> str:
        """
        :description: 最长公共前缀，字符串匹配，算法优化
        """
        if not strs:
            return ""
        length, count = len(strs[0]), len(strs)
        for i in range(length):
            c = strs[0][i]
            if any(i == len(strs[j]) or strs[j][i] != c for j in range(1, count)):
                return strs[0][:i]

        return strs[0]

    def isValid_1(self, s: str) -> bool:
        """
        :description: 有效的括号，遍历匹配
        :param s: 只含括号的字符串
        :return: bool
        """
        list_1, str_1 = [], ""
        for i in range(len(s)):
            if s[i] == '{' or s[i] == '[' or s[i] == '(':
                list_1.append(s[i])
            elif s[i] == '}':
                if len(list_1) == 0:
                    return False
                else:
                    str_1 = list_1.pop(-1)
                    if str_1 != '{':
                        return False

            elif s[i] == ']':
                if len(list_1) == 0:
                    return False
                else:
                    str_1 = list_1.pop(-1)
                    if str_1 != '[':
                        return False

            elif s[i] == ')':
                if len(list_1) == 0:
                    return False
                else:
                    str_1 = list_1.pop(-1)
                    if str_1 != '(':
                        return False
        return len(list_1) == 0

    def isValid_2(self, s: str) -> bool:
        """
        :description: 有效的括号，利用字典匹配
        :param s: 只含括号的字符串
        :return: bool
        """
        if len(s) % 2 == 1:
            return False
        else:
            pairs = {")": "(", "]": "[", "}": "{"}
            list_1 = []
            for ch in s:
                if ch in pairs:
                    if not list_1 or list_1[-1] != pairs[ch]:
                        return False
                    list_1.pop()
                else:
                    list_1.append(ch)
            return not list_1

    def removeDuplicates(self, nums: List[int]) -> int:
        """
        :description: 删除有序数组中的重复项，双指针
        """
        if not nums:
            return 0
        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i = i + 1
                nums[i] = nums[j]
        return i+1

    def removeElement_1(self, nums: List[int], val: int) -> int:
        """
        :description: 移除数组中的指定元素，双指针，val后移
        :param nums:
        :param val:
        :return:
        """
        i, count = 0, len(nums)
        while i < count:
            if nums[i] == val:
                nums[i] = nums[count-1]
                count -= 1
            else:
                i += 1

        return count

    def removeElement_2(self, nums: List[int], val: int) -> int:
        """
        :description: 移除数组中的指定元素，双指针，元素前移
        :param nums:
        :param val:
        :return:
        """
        a, b = 0, 0

        while a < len(nums):
            if nums[a] != val:
                nums[b] = nums[a]
                b += 1
            a += 1

        return b

    def strStr(self, haystack: str, needle: str) -> int:
        """
        :description: 实现strStr() 函数
        :param haystack:
        :param needle:
        :return:
        """
        if needle == "":
            return 0
        elif needle != "" and haystack == "":
            return -1
        else:
            len_1, len_2 = len(haystack), len(needle)
            for i in range(len_1):
                if haystack[i] == needle[0]:
                    if i + len_2 <= len_1:
                        if haystack[i:i+len_2] == needle:
                            return i
            return -1

    def searchInsert_1(self, nums: List[int], target: int) -> int:
        """
        :description: 搜索插入位置，暴力破解
        :param nums:
        :param target:
        :return:
        """
        if not nums:
            return 0
        for i in range(0, len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

    def searchInsert_2(self, nums: List[int], target: int) -> int:
        """
        :description: 搜索插入位置，二分查找
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left
