from solution import Solution

if __name__ == '__main__':
    solution = Solution()  # 调用类时，先进行类的初始化
    nums = [2, 7, 11, 15]
    target = 9
    print(solution.twoSum_2(nums, target))
