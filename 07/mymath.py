def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

def fibonacci(n):
    fibs = []
    a, b = 1, 1
    for _ in range(n):
        fibs.append(a)
        a, b = b, a + b
    return fibs

def is_perfect(n):
    if n < 2:
        return False
    sums = sum(i for i in range(1, n) if n % i == 0)
    return sums == n

if __name__ == "__main__":
    print("===== 数学工具包测试 =====\n")
    
    print("素数判断：")
    print(f"7是素数: {is_prime(7)}")
    print(f"10不是素数: {is_prime(10)}\n")
    
    print("阶乘：")
    print(f"5! = {factorial(5)}\n")
    
    print("最大公约数和最小公倍数：")
    a, b = 24, 36
    print(f"gcd({a}, {b}) = {gcd(a, b)}")
    print(f"lcm({a}, {b}) = {lcm(a, b)}\n")
    
    print("斐波那契数列：")
    n = 10
    print(f"前{n}项：{', '.join(map(str, fibonacci(n)))}\n")
    
    print("完全数判断：")
    print(f"6是完全数: {is_perfect(6)}")
    print(f"28是完全数: {is_perfect(28)}")
