# 高级数学运算模块
# 包含阶乘、斐波那契数列等高级数学功能

def factorial(n):
    """计算阶乘 n!"""
    if n < 0:
        raise ValueError("阶乘仅支持非负整数")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def fibonacci(n):
    """计算斐波那契数列第 n 项（从 0 开始计数）"""
    if n < 0:
        raise ValueError("斐波那契数列索引不能为负")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def is_prime(n):
    """判断一个数是否为质数"""
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("=== 高级数学运算 ===")
    print(f"5! = {factorial(5)}")
    print(f"斐波那契第10项 = {fibonacci(10)}")
    print(f"17 是质数吗？ {is_prime(17)}")
    print(f"15 是质数吗？ {is_prime(15)}")
