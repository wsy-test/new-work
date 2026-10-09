# 简单计算器
# 实现基本的加减乘除运算

def add(a, b):
    """加法运算"""
    return a + b

def subtract(a, b):
    """减法运算"""
    return a - b

def multiply(a, b):
    """乘法运算"""
    return a * b

def divide(a, b):
    """除法运算"""
    if b == 0:
        raise ValueError("除数不能为零")
    return a / b

def power(a, b):
    """幂运算：计算 a 的 b 次方"""
    return a ** b

def modulus(a, b):
    """取模运算：计算 a 除以 b 的余数"""
    if b == 0:
        raise ValueError("模数不能为零")
    return a % b

if __name__ == "__main__":
    print("=== 简单计算器 ===")
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"20 / 4 = {divide(20, 4)}")
    print(f"2^10 = {power(2, 10)}")
    print(f"17 % 5 = {modulus(17, 5)}")
