from solution_simple import Solution as SolutionSimple
from solution_middle import Solution as SolutionMiddle
# 利用 as 调用两个同名的类，解决冲突


if __name__ == '__main__':
    solution = SolutionSimple()  # 调用类时，先进行类的初始化
    num = 5
    g = [4,1,2]
    s = [1,3,4,2]
    print(solution.nextGreaterElement(g,s))

