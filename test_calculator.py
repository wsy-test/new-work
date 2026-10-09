# 单元测试文件
# 对计算器和高级数学模块进行测试

import sys
sys.path.insert(0, '.')

from calculator import add, subtract, multiply, divide, power, modulus
from advanced_math import factorial, fibonacci, is_prime

def test_calculator():
    """测试基础计算器功能"""
    assert add(3, 5) == 8, "加法测试失败"
    assert subtract(10, 4) == 6, "减法测试失败"
    assert multiply(6, 7) == 42, "乘法测试失败"
    assert divide(20, 4) == 5, "除法测试失败"
    assert power(2, 10) == 1024, "幂运算测试失败"
    assert modulus(17, 5) == 2, "取模测试失败"
    
    # 测试除零异常
    try:
        divide(10, 0)
        assert False, "除零应该抛出异常"
    except ValueError:
        pass
    
    print("✅ 基础计算器测试全部通过")

def test_advanced_math():
    """测试高级数学功能"""
    assert factorial(0) == 1, "0的阶乘应为1"
    assert factorial(1) == 1, "1的阶乘应为1"
    assert factorial(5) == 120, "5的阶乘应为120"
    
    assert fibonacci(0) == 0, "斐波那契第0项应为0"
    assert fibonacci(1) == 1, "斐波那契第1项应为1"
    assert fibonacci(10) == 55, "斐波那契第10项应为55"
    
    assert is_prime(2) == True, "2是质数"
    assert is_prime(17) == True, "17是质数"
    assert is_prime(15) == False, "15不是质数"
    assert is_prime(1) == False, "1不是质数"
    
    print("✅ 高级数学测试全部通过")

if __name__ == "__main__":
    print("=== 运行单元测试 ===")
    test_calculator()
    test_advanced_math()
    print("\n🎉 所有测试通过！")
