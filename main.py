from solution_simple import Solution as SolutionSimple
from solution_middle import Solution as SolutionMiddle
# 利用 as 调用两个同名的类，解决冲突


if __name__ == '__main__':
    solution = SolutionSimple()  # 调用类时，先进行类的初始化
    # print(solution.toHex(12))
    num = -9
    print(bin(num))
    # print(bin(0xff))
    num &= 0b11111111
    print(bin(num))
