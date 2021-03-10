# -*- coding: utf-8 -*-
# @File : solution_simple.py
# @Description：简单算法
# @Author : 杨睿
# @Time : 2021-01-14 23:21
import collections
from functools import reduce
from typing import *
import math


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

    def countAndSay(self, n: int) -> str:
        """
        :description: 输出外观数列的第 n 项
        :param n:
        :return:
        """
        if n == 1:
            return "1"
        else:
            str_num = "1"
            for i in range(n-1):
                str_num = Solution.description(str_num)
            return str_num

    @classmethod
    def description(cls, str_num: str) -> str:
        """
        方法用于：被 countAndSay 调用，描述num
        """
        val = str_num[0]
        return_str = ""
        j = 0
        for i in range(len(str_num)):
            if str_num[i] == val:
                j += 1
            else:
                return_str = return_str + str(j) + val
                val = str_num[i]
                j = 1

        # 解决 “11” 这种情况
        return_str = return_str + str(j) + val
        return return_str

    def maxSubArray_1(self, nums: List[int]) -> int:
        """
        :description: 最大子序和，动态规划
        :param nums: list[int]
        :return: int
        """
        pre, max_ans = 0, nums[0]
        for i in nums:
            pre = max(pre+i, i)
            max_ans = max(max_ans, pre)

        return max_ans

    def maxSubArray_2(self, nums: List[int]) -> int:
        """
        :description: 最大子序和，分治
        :param nums: list[int]
        :return: int
        """
        n = len(nums)
        # 递归终止条件
        if n == 1:
            return nums[0]
        else:
            # 递归计算左半边最大子序和
            max_left = self.maxSubArray(nums[0:len(nums) // 2])
            # 递归计算右半边最大子序和
            max_right = self.maxSubArray(nums[len(nums) // 2:len(nums)])

        # 计算中间的最大子序和，从右到左计算左边的最大子序和，从左到右计算右边的最大子序和，再相加
        max_l = nums[len(nums) // 2 - 1]
        tmp = 0
        for i in range(len(nums) // 2 - 1, -1, -1):
            tmp += nums[i]
            max_l = max(tmp, max_l)
        max_r = nums[len(nums) // 2]
        tmp = 0
        for i in range(len(nums) // 2, len(nums)):
            tmp += nums[i]
            max_r = max(tmp, max_r)
        # 返回三个中的最大值
        return max(max_right, max_left, max_l + max_r)

    def lengthOfLastWord(self, s: str) -> int:
        """
        :description: 最后一个单词的长度
        :param s: str
        :return: int
        """
        length, j = 0, -1
        for i in range(len(s)):
            if s[j] == " ":
                if length == 0:
                    j -= 1
                else:
                    return length
            else:
                length += 1
                j -= 1
        return length

    def plusOne(self, digits: List[int]) -> List[int]:
        """
        :description: 加一
        :param digits: list
        :return: list
        """
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1
            if digits[i] != 10:
                break
            else:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
        return digits

    def addBinary(self, a: str, b: str) -> str:
        """
        :description: 计算两个二进制数的和
        :param a:
        :param b:
        :return:
        """
        # 1. 补齐两个字符串，使得两个字符串一样长
        if len(a) < len(b):
            a = '0'*(len(b)-len(a))+a
        else:
            b = '0'*(len(a)-len(b))+b
        # carry 记录 是否进位，res 记录 返回的字符串
        carry = 0
        res = ''
        for i in range(len(a)-1, -1, -1):
            if int(a[i])+int(b[i])+carry >= 2:
                res = str(int(a[i])+int(b[i])+carry-2)+res
                carry = 1
            else:
                res = str(int(a[i])+int(b[i])+carry)+res
                carry = 0
        if carry == 1:
            res = '1'+res
        return res

    def mySqrt_1(self, x: int) -> int:
        """
        :description: 求 x 的平方根，数学公式
        :param x:
        :return:
        """
        if x == 0:
            return 0
        ans = int(math.exp(0.5 * math.log(x)))
        return ans + 1 if (ans + 1) ** 2 <= x else ans

    def mySqrt_2(self, x: int) -> int:
        """
        :description: 求 x 的平方根，二分查找
        :param x:
        :return:
        """
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l+r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid-1
        return ans

    def mySqrt_3(self, x: int) -> int:
        """
        :description: 求 x 的平方根，牛顿迭代
        :param x:
        :return:
        """
        if x == 0:
            return 0
        c, x_0 = float(x), float(x)
        while True:
            x_i = 0.5 * (x_0 + c / x_0)
            if abs(x_0 - x_i) < 1e-7:
                break
            x_0 = x_i

        return int(x_0)

    def generate_1(self, numRows: int) -> List[List[int]]:
        """
        :description: 杨辉三角
        :param numRows:
        :return:
        """
        res_list = []
        pre_list = []
        for i in range(1, numRows+1):
            pre_list = Solution.generate_list(pre_list, i)
            res_list.append(pre_list)
        return res_list

    @classmethod
    def generate_list(cls, pre_list: List[int], length: int) -> List[int]:
        res_list = []
        if length == 1:
            res_list = [1]
        elif length == 2:
            res_list = [1, 1]
        else:
            res_list = [1, 1]
            for i in range(1, length-1):
                num = pre_list[i-1] + pre_list[i]
                res_list.insert(i, num)
        return res_list

    def generate_2(self, numRows: int) -> List[List[int]]:
        """
        :description: 杨辉三角
        :param numRows:
        :return:
        """
        ret = list()
        for i in range(numRows):
            row = list()
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(ret[i - 1][j] + ret[i - 1][j - 1])
            ret.append(row)
        return ret

    def getRow_1(self, rowIndex: int) -> List[int]:
        """
        :description: 杨辉三角，获取指定行
        :param rowIndex: int
        :return: list[int]
        """
        pre_list = []
        for i in range(rowIndex):
            res_list = list()
            for j in range(0, i+1):
                if j == 0 or j == i:
                    res_list.append(1)
                else:
                    res_list.append(pre_list[j-1] + pre_list[j])
            pre_list = res_list
        return pre_list

    def getRow_2(self, rowIndex: int) -> List[int]:
        """
        :description: 杨辉三角，获取指定行
        :param rowIndex: int
        :return: list[int]
        """
        res_list = [1] * (rowIndex+1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                res_list[j] = res_list[j] + res_list[j-1]
        return res_list
            
    def maxProfit_1(self, prices: List[int]) -> int:
        """
        :description: 买卖股票的最佳时机
        :param prices:
        :return:
        """
        i, profit = 0, 0
        for j in range(1, len(prices)):
            if prices[j] > prices[i]:
                if profit < prices[j] - prices[i]:
                    profit = prices[j] - prices[i]
            else:
                i = j
        return profit

    def maxProfit(self, prices: List[int]) -> int:
        """
        :description: 买卖股票的最佳时机，进阶
        :param prices:
        :return:
        """
        if len(prices) == 0:
            return 0
        else:
            i, profit = 0, 0
            prices.append(0)
            for j in range(len(prices)):
                if prices[j] > prices[i] and prices[j] > prices[j+1]:
                    profit = profit + prices[j] - prices[i]
                    i = j+1
                if prices[j] < prices[i]:
                    i = j
            return profit

    def maxProfit_2(self, prices: List[int]) -> int:
        """
        :description: 买卖股票的最佳时机，进阶，贪心算法
        :param prices:
        :return:
        """
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

    def isPalindrome(self, s: str) -> bool:
        """
        :description: 判断是否为 回文串
        :param s:
        :return:
        """
        i, j = 0, len(s)-1
        while i < j:
            # isalnum：库函数。判断传入的字符是否为字母或数字
            # 加入 i<j 的判定条件，防止出现 i或者j 溢出的情况
            # 例如：s = "    "
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if i < j:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
        return True

    def singleNumber(self, nums: List[int]) -> int:
        """
        :description: 只出现一次的数字，位运算
        :param nums:
        :return:
        """
        # lambda：创建匿名函数
        # X ^ y : 实现 异或运算
        # reduce: 库函数
        return reduce(lambda x, y: x ^ y, nums)

    def convertToTitle(self, n: int) -> str:
        """
        :description: Excel表，列名称
        :param n:
        :return:
        """
        s = ""
        while n > 0:
            n -= 1
            a, b = n // 26, n % 26
            s = s + chr(b+65)
            n = a
        return s[::-1]

    def trailingZeroes(self, n: int) -> int:
        """
        :description: 阶乘后的 0
        :param n:
        :return:
        """
        zero_count = 0
        while n > 0:
            n //= 5
            zero_count += n
        return zero_count

    def reverseBits(self, n: int) -> int:
        """
        :description：颠倒二进制位
        :param n:
        :return:
        """
        ret, power = 0, 31
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power -= 1
        return ret

    def hammingWeight_1(self, n: int) -> int:
        """
        :description: 位1 的个数
        :param n:
        :return:
        """
        count = 0
        while n:
            if (n & 1) == 1:
                count += 1
            n = n >> 1
        return count

    def hammingWeight_2(self, n: int) -> int:
        """
        :description: 位1 的个数
        :param n:
        :return:
        """
        count = 0
        while n:
            count += 1
            n &= (n-1)
        return count

    def isHappy_1(self, n: int) -> bool:
        """
        :description: 快乐数，哈希集合检测循环
        :param n:
        :return:
        """
        res = 0
        seen = set()
        while 1 <= n < (2 ** 32)-1:
            res = 0
            while n != 0:
                n, digit = divmod(n, 10)
                res += digit**2
                # res += (n % 10)**2
                # n = (n // 10)
            n = res
            if n == 1:
                return True
            elif n != 1 and n not in seen:
                seen.add(n)
            else:
                return False

    def isHappy_2(self, n: int) -> bool:
        """
        :description: 快乐数，哈希集合检测循环，内置def
        :param n:
        :return:
        """
        def get_next(num):
            total_sum = 0
            while num > 0:
                num, digit = divmod(num, 10)
                total_sum += digit ** 2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1

    def isHappy_3(self, n: int) -> bool:
        """
        :description: 快乐数，快慢指针
        :param n:
        :return:
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1

    def countPrimes_1(self, n: int) -> int:
        """
        :description: 计数质数，暴力破解
        :param n:
        :return:
        """
        def is_prime(num: int) -> bool:
            i = 2
            while i**2 <= num:
                if num % i == 0:
                    return False
                i += 1
            return True

        ans, i = 0, 2
        while i < n:
            ans += is_prime(i)
            i += 1
        return ans

    def countPrimes_2(self, n: int) -> int:
        """
        :description: 计数质数，埃氏筛
        :param n:
        :return:
        """
        # 定义数组标记是否是质数
        is_prime = [1] * n
        count = 0
        for i in range(2, n):
            # 将质数的倍数标记为合数
            if is_prime[i]:
                count += 1
                # 从 i*i 开始标记
                for j in range(i * i, n, i):
                    is_prime[j] = 0
        return count

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        :description: 同构字符串，哈希表实现双射
        :param s:
        :param t:
        :return:
        """
        hashmap1 = {}
        hashmap2 = {}
        for c1, c2 in zip(s, t):
            if hashmap1.get(c1, c2) != c2 or hashmap2.get(c2, c1) != c1:
                return False
            hashmap1[c1] = c2
            hashmap2[c2] = c1
        return True

    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :description: 存在重复的元素
        :param nums:
        :return:
        """
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        :description: 存在重复元素||
        :param nums:
        :param k:
        :return:
        """
        seen = dict()
        for i, num in enumerate(nums):
            if seen.get(num) is not None:
                if i-seen.get(num) <= k:
                    return True
                else:
                    seen[num] = i
            else:
                seen[num] = i
        return False

    def summaryRanges(self, nums: List[int]) -> List[str]:
        """
        :description: 汇总区间
        :param nums:
        :return:
        """
        if nums is None:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            i, j, length, range_str = 0, 1, len(nums), ""
            ranges = list()
            while j < length:
                if nums[j] - nums[j-1] == 1:
                    j += 1
                else:
                    if i == j-1:
                        range_str = str(nums[i])
                    else:
                        range_str = str(nums[i]) + "->" + str(nums[j-1])
                    ranges.append(range_str)
                    i = j
                    j += 1
            if i != j-1:
                range_str = str(nums[i]) + "->" + str(nums[j - 1])
            else:
                range_str = str(nums[i])
            ranges.append(range_str)
            return ranges

    def isPowerOfTwo_1(self, n: int) -> bool:
        """
        :description: 2的幂，暴力破解
        :param n:
        :return:
        """
        if n <= 0:
            return False
        while n % 2 == 0:
            n /= 2
        return n == 1

    def isPowerOfTwo_2(self, n: int) -> bool:
        """
        :description: 2的幂，位运算，获取二进制中最右边的 1
        :param n:
        :return:
        """
        if n <= 0:
            return False
        return n & (-n) == n

    def isPowerOfTwo_3(self, n: int) -> bool:
        """
        :description: 2的幂，位运算，去除二进制中最右边的 1
        :param n:
        :return:
        """
        if n <= 0:
            return False
        return n & (n-1) == 0

    def isAnagram_1(self, s: str, t: str) -> bool:
        """
        :description: 字母异位词，排序
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        s = sorted(s)
        t = sorted(t)
        return s == t

    def isAnagram_2(self, s: str, t: str) -> bool:
        """
        :description: 字母异位词，哈希
        :param s:
        :param t:
        :return:
        """
        if len(s) != len(t):
            return False
        count = [0]*26  # 生成一个长度为 26 的列表
        for i in s:
            count[ord(i) - ord("a")] += 1  # ord() 函数可将 字符 转成 10进制，方便进行 ASCII码 的计算
        for i in t:
            count[ord(i) - ord("a")] -= 1
            if count[ord(i) - ord("a")] < 0:
                return False
        return True

    def addDigits_1(self, num: int) -> int:
        """
        :description: 各位相加，循环
        :param num:
        :return:
        """
        digit = 0
        while num > 9:
            digit = num % 10
            num //= 10
            num += digit
        return num

    def addDigits_2(self, num: int) -> int:
        """
        :description: 各位相加，数学定义
        :param num:
        :return:
        """
        if num == 0:
            return 0
        return (num-1) % 9 + 1

    def isUgly(self, num: int) -> bool:
        """
        :description: 丑数
        :param num:
        :return:
        """
        if num < 1:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        return num == 1

    def missingNumber_1(self, nums: List[int]) -> int:
        """
        :description: 丢失的数字，位运算
        :param nums:
        :return:
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= (i ^ num)
        return missing

    def missingNumber_2(self, nums: List[int]) -> int:
        """
        :description: 丢失的数字，数学公式
        :param nums:
        :return:
        """
        missing = len(nums)
        for i, num in enumerate(nums):
            missing += i - num
        return missing

    def moveZeroes(self, nums: List[int]) -> None:
        """
        :description: 移动 0
        :param nums:
        :return:
        """
        n = len(nums)
        left, right = 0, 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

    def wordPattern(self, pattern: str, s: str) -> bool:
        """
        :description: 单词规律
        :param pattern:
        :param s:
        :return:
        """
        params = list()
        param = ""
        for i in s:
            if i != " ":
                param += i
            else:
                params.append(param)
                param = ""
        params.append(param)
        if len(params) != len(pattern):
            return False
        dict_1 = {}
        dict_2 = {}
        for x, y in zip(pattern, params):
            if dict_1.get(x, y) != y or dict_2.get(y, x) != x:
                return False
            dict_1[x] = y
            dict_2[y] = x
        return True

    def isPowerOfThree(self, n: int) -> bool:
        """
        :description: 3的幂
        :param n:
        :return:
        """
        if n <= 0:
            return False
        return (math.log10(n) / math.log10(3)) % 1 == 0

    def reverseString(self, s: List[str]) -> None:
        """
        :description: 反转字符串
        :param s:
        :return:
        """
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

    def reverseVowels(self, s: str) -> str:
        """
        :description: 反转元音字母
        :param s:
        :return:
        """
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left, right, list_s = 0, len(s)-1, list(s)
        while left < right:
            while list_s[left] not in vowels and left < right:
                left += 1
            while list_s[right] not in vowels and left < right:
                right -= 1
            if left < right:
                char = list_s[left]
                list_s[left] = list_s[right]
                list_s[right] = char
                left += 1
                right -= 1
            else:
                break
        return "".join(list_s)

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :description: 两个数组的交集
        :param nums1:
        :param nums2:
        :return:
        """
        set_1 = set(nums2)
        set_2 = set()
        for i in nums1:
            if i in set_1 and i not in set_2:
                set_2.add(i)
        return list(set_2)

    def intersect_1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :description: 求两个数组的交集 2，哈希表
        :param nums1:
        :param nums2:
        :return:
        """
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)  # python 递归

        dict_1 = collections.Counter(nums1)  # collections.Counter() 计数器
        list_1 = list()
        for num in nums2:
            if dict_1[num] != 0:
                list_1.append(num)
                dict_1[num] -= 1
                if dict_1[num] == 0:
                    dict_1.pop(num)

        return list_1

    def intersect_2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        :description: 求两个数组的交集 2，排序+双指针
        :param nums1:
        :param nums2:
        :return:
        """
        nums1.sort()
        nums2.sort()
        intersection = list()
        len_1, len_2 = len(nums1), len(nums2)
        index_1 = index_2 = 0
        while index_1 < len_1 and index_2 < len_2:
            if nums1[index_1] < nums2[index_2]:
                index_1 += 1
            elif nums1[index_1] > nums2[index_2]:
                index_2 += 1
            else:
                intersection.append(nums1[index_1])
                index_2 += 1
                index_1 += 1

        return intersection

    def isPerfectSquare_1(self, num: int) -> bool:
        """
        :description: 有效的完全平方数，数学公式
        :param num:
        :return:
        """
        ans = int(math.exp(0.5 * math.log(num)))
        return ans**2 == num or (ans+1)**2 == num

    def isPerfectSquare_2(self, num: int) -> bool:
        """
        :description: 有效的完全平方数，二分查找
        :param num:
        :return:
        """
        left, right = 1, (num//2 + 1)
        while left < right:
            mid = left + (right-left) // 2
            if mid**2 > num:
                right = mid
            elif mid**2 < num:
                left = mid + 1
            else:
                return True
        return left**2 == num

    def getSum(self, a: int, b: int) -> int:
        """
        :description: 两整数之和，位运算
        :param a:
        :param b:
        :return:
        """
        # 2^32
        MASK = 0x100000000
        # 整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            # 计算进位
            carry = (a & b) << 1
            # 取余范围限制在 [0, 2^32-1] 范围内
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

    def guessNumber(self, n: int) -> int:
        """
        :description: 猜数字游戏，二分查找
        :param n:
        :return:
        """
        def guess(num: int):
            pass

        left, right = 1, n
        while left < right:
            mid = (left + right) >> 1
            if guess(mid) == -1:
                right = mid
            elif guess(mid) == 1:
                left = mid+1
            else:
                return mid
        return left

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        """
        :description: 赎金信
        :param ransomNote:
        :param magazine:
        :return:
        """
        magazine_dict = collections.Counter(magazine)
        for i in ransomNote:
            if i in magazine_dict:
                magazine_dict[i] -= 1
                if magazine_dict[i] < 0:
                    return False
            else:
                return False
        return True

    def firstUniqChar_1(self, s: str) -> int:
        """
        :description: 字符串中第一个唯一字符，两次遍历，哈希表
        :param s:
        :return:
        """
        dict_1 = collections.Counter(s)
        for i, char in enumerate(s):
            if dict_1[char] == 1:
                return i
        return -1
        
    def firstUniqChar_2(self, s: str) -> int:
        """
        :description: 字符串中第一个唯一字符，两次遍历，哈希表
        :param s:
        :return:
        """
        dict_1 = dict()
        for i, char in enumerate(s):
            if char not in dict_1:
                dict_1[char] = i
            else:
                dict_1[char] = -1
        for char in dict_1:
            if dict_1[char] != -1:
                return dict_1[char]
        return -1

    def findTheDifference(self, s: str, t: str) -> str:
        """
        :description: 找不同，哈希表
        :param s:
        :param t:
        :return:
        """
        dict_s = collections.Counter(s)
        for char in t:
            if char not in dict_s:
                return char
            else:
                dict_s[char] -= 1
                if dict_s[char] == 0:
                    dict_s.pop(char)

    def findTheDifference_2(self, s: str, t: str) -> str:
        """
        :description: 找不同，位运算
        :param s:
        :param t:
        :return:
        """
        res = 0
        for i in s:
            res ^= ord(i)
        for i in t:
            res ^= ord(i)
        return chr(res)

    def isSubsequence(self, s: str, t: str) -> bool:
        """
        :description: 判断子序列，双指针
        :param s:
        :param t:
        :return:
        """
        i, j, len_s, len_t = 0, 0, len(s), len(t)
        while i < len_s and j < len_t:
            if t[j] == s[i]:
                j += 1
                i += 1
            else:
                j += 1
        return i == len_s

    def toHex(self, num: int) -> str:
        """
        :description: 将一个整数转换为 16进制
        :param num:
        :return:
        """
        num &= 0xFFFFFFFF  # 数字在计算机中都是以其补码的形式进行存储的，进行位运算也是其补码进行位运算
        s = "0123456789abcdef"
        res = ""
        mask = 0b1111
        while num > 0:
            res += s[num & mask]  # 获取 num 低4位 的 值
            num >>= 4
        return res[::-1] if res else "0"

    def longestPalindrome(self, s: str) -> int:
        """
        :description: 最长回文串
        :param s:
        :return:
        """
        # 哈希表记录各个字符出现的次数
        dict_str = collections.Counter(s)
        ans, count = 0, 0  # ans 表示返回值，count标记是否出现 奇次数的字符
        for key in dict_str:
            if dict_str[key] % 2 == 0:
                ans += dict_str[key]  # 字符出现次数为偶数
            else:
                ans += (dict_str[key]-1)  # 字符出现的次数为奇数
                count = 1  # 标记出现过奇数
        return ans + count

    def fizzBuzz(self, n: int) -> List[str]:
        """
        :description: Fizz Buzz，字符串拼接
        :param n:
        :return:
        """
        ans_list = list()
        for i in range(1, n+1):
            ans_str = ""  # 映射字符串
            divisible_by_3 = (i % 3 == 0)
            divisible_by_5 = (i % 5 == 0)
            """
            用两个 if 条件，实现 3个 判定条件
            （1）i 只是 3 的倍数，ans = "", ans += "Fizz"
            （2）i 只是 5 的倍数，ans = "", ans += "Buzz"
            （3）i 同时是 3 和 5 的倍数，ans = "Fizz", ans += "Buzz"
            """
            if divisible_by_3:
                ans_str += "Fizz"
            if divisible_by_5:
                ans_str += "Buzz"
            if not ans_str:
                ans_str = str(i)
            ans_list.append(ans_str)
        return ans_list

    def thirdMax(self, nums: List[int]) -> int:
        """
        :description: 第三大的数
        :param nums:
        :return:
        """
        first = second = third = float('-inf')
        for num in nums:
            if num > first:
                third = second
                second = first
                first = num
            elif num > second and num != first:
                third = second
                second = num
            elif num > third and num != second and num != first:
                third = num
        return first if math.isinf(third) else third

    def addStrings(self, num1: str, num2: str) -> str:
        """
        :description: 字符串相加
        :param num1:
        :param num2:
        :return:
        """
        i, j, add, res = len(num1)-1, len(num2)-1, 0, ""
        while i >= 0 or j >= 0:
            # 补0 操作，短的字符串遍历结束后，在高位进行补0，使得遍历正常进行
            n1 = int(num1[i]) if i >= 0 else 0
            n2 = int(num2[j]) if j >= 0 else 0

            tmp = n1 + n2 + add
            add = tmp // 10
            res = str(tmp % 10) + res
            i, j = i-1, j-1
        return "1" + res if add == 1 else res

    def countSegments(self, s: str) -> int:
        """
        :description: 字符串中的单词数
        :param s:
        :return:
        """
        count = 0
        for i in range(len(s)):
            if (i == 0 or s[i-1] == " ") and s[i] != " ":
                count += 1
        return count

    def arrangeCoins(self, n: int) -> int:
        """
        :description: 硬币排列
        :param n:
        :return:
        """
        if n == 0:
            return 0
        
        left, right = 0, n
        while left < right:
            mid = left + (right-left) // 2
            """
            注意：mid 的正确条件是：(1+mid)*mid <= 2n < (2+mid)*(mid+1)
            因此与之相反的条件是：(1+mid)*mid > 2n 或者 (2+mid)*(mid+1) <= 2n
            """
            if (1+mid)*mid > 2*n:
                right = mid - 1
            elif (2+mid)*(mid+1) <= 2*n:
                left = mid + 1
            else:
                return mid
        return left

    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        :description: 找到数组中消失的数字，原地法
        :param nums:
        :return:
        """
        n = len(nums)
        for num in nums:
            x = (num-1) % n  # 找到数 x
            nums[x] += n  # 修改索引为 x 的数的值，以此标记 数x 在数组中

        ret = [i+1 for i, num in enumerate(nums) if num <= n]
        return ret

    def minMoves_1(self, nums: List[int]) -> int:
        """
        :description: 最小操作次数使得数组元素相等，动态规划
        :param nums:
        :return:
        """
        list.sort(nums)
        moves = 0
        for i in range(1, len(nums)):
            diff = (moves + nums[i]) - nums[i-1]
            nums[i] += moves
            moves += diff
        return moves

    def minMoves_2(self, nums: List[int]) -> int:
        """
        :description: 最小操作次数使得数组元素相等，数学法
        :param nums:
        :return:
        """
        min_num = min(nums)
        moves = 0
        for i in range(len(nums)):
            moves += (nums[i] - min_num)
        return moves

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        :description: 分发饼干，排序+贪心
        :param g:
        :param s:
        :return:
        """
        list.sort(g)
        list.sort(s)
        i, j, g_len, s_len = 0, 0, len(g), len(s)
        count = 0
        while i < g_len and j < s_len:
            while g[i] > s[j] and j < s_len:
                j += 1
                if j == s_len:
                    return count
            count += 1
            i += 1
            j += 1
        return count


            

            



