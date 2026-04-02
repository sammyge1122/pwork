for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j:<4}", end=" ")
    print()
xz=input("是否打印倒序乘法表？（y/n）：")
if xz == 'y' or xz == 'Y':
    for i in range(9, 0, -1):
        for j in range(1, i + 1):
            print(f"{j}×{i}={i*j:<4}", end=" ")
        print()