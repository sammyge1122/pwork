import  mymath
if __name__ == "__main__":
    
    print("素数判断：")
    print(f"7是素数: {mymath.is_prime(7)}")
    print(f"10不是素数: {mymath.is_prime(10)}\n")
    
    print("阶乘：")
    print(f"5! = {mymath.factorial(5)}\n")
    
    print("最大公约数和最小公倍数：")
    a, b = 24, 36
    print(f"gcd({a}, {b}) = {mymath.gcd(a, b)}")
    print(f"lcm({a}, {b}) = {mymath.lcm(a, b)}\n")
    
    print("斐波那契数列：")
    n = 10
    print(f"前{n}项：{', '.join(map(str, mymath.fibonacci(n)))}\n")
    
    print("完全数判断：")
    print(f"6是完全数: {mymath.is_perfect(6)}")
    print(f"28是完全数: {mymath.is_perfect(28)}")