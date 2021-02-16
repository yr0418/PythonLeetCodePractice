from solution_simple import Solution as SolutionSimple
from solution_middle import Solution as SolutionMiddle
# 利用 as 调用两个同名的类，解决冲突


if __name__ == '__main__':
    solution = SolutionSimple()  # 调用类时，先进行类的初始化
    prices = [7, 10, 1, 3, 6, 4]
    print(solution.maxProfit(prices))
