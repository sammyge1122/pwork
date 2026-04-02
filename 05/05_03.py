import random

def chuangjian(a_x, a_y):
    return [[random.randint(1, 10) for _ in range(a_y)] for _ in range(a_x)]
def xianshi(a):
    for r in a:
        print(r)
def T(a):
    return [[a[j][i] for j in range(len(a))] for i in range(len(a[0]))]
def jia(a, b):
    if len(a) != len(b) or len(a[0]) != len(b[0]):
        print("矩阵维度不同，无法进行加法运算")
        return None
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]
def cheng(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(a[0]))) for j in range(len(b[0]))] for i in range(len(a))]



a_x=int(input("请输入第一个矩阵的行数："))
a_y=int(input("请输入第一个矩阵的列数："))
b_x=int(input("请输入第二个矩阵的行数："))
b_y=int(input("请输入第二个矩阵的列数："))
A=chuangjian(a_x, a_y)
B=chuangjian(b_x, b_y)
print("\n矩阵A ({}×{}):".format(a_x, a_y))
xianshi(A)
print("\n矩阵B ({}×{}):".format(b_x, b_y))  
xianshi(B)
print("\n===== 矩阵转置 =====")
print("矩阵A的转置 ({}×{}):".format(a_y, a_x))
xianshi(T(A))
print("\n矩阵B的转置 ({}×{}):".format(b_y, b_x))
xianshi(T(B))
print("\n===== 矩阵加法 =====")
jia_r = jia(A, B)
if jia_r is not None:
    print("矩阵A + 矩阵B ({}×{}):".format(a_x, a_y))
    xianshi(jia_r)
print("\n===== 矩阵乘法 =====")
cheng_r = cheng(A, B)
print("矩阵A × 矩阵B ({}×{}):".format(a_x, b_y))
xianshi(cheng_r)