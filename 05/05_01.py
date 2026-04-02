import random
a=[random.randint(1, 100) for _ in range(10)]
print("原始列表：",a)
print("第一个元素：",a[0])
print("最后一个元素：",a[-1])
print("前5个元素:",a[:5])
print("后3个元素:",a[-3:])
a[2]=999
print("修改第3个元素后:",a)
a.append(random.randint(1, 100))
print("添加新元素后：",a)
for i in range(len(a)):
    if a[i]%2==0:
        a.pop(i)
        break
print("删除第一个偶数后：",a)
print("最终列表：",a)
b=a[::-1]
print("反转后列表（新列表）：",b)