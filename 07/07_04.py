
products = {"苹果": 5, "香蕉": 3, "橙子": 4, "牛奶": 8, "面包": 6}
cart = []
balance = 50

def show_products():
    print("\n商品列表：")
    for product, price in products.items():
        print(f"{product}: {price}元")

def show_cart():
    print("\n购物车内容：")
    zhongjia = 0
    print(cart)
    zhongjia = sum(products[item] for item in cart)
    print(f"总价：{zhongjia}元")

def add_to_cart(product_name):
    global cart
    if product_name in products:
        cart.append(product_name)
        print(f"已添加：{product_name}")
    else:
        print("商品不存在")

def remove_from_cart(product_name):
    global cart
    if product_name in cart:
        cart.remove(product_name)
        print(f"已移除：{product_name}")
    else:
        print("商品不在购物车中")

def checkout():
    global cart, balance
    zhongjia = sum(products[item] for item in cart)
    if zhongjia <= balance:
        balance -= zhongjia
        print("正在结算...")
        show_cart()
        print("结算成功！剩余余额：", balance)
        cart = []
    else:
        print("余额不足")

def recharge(amount):
    global balance
    balance += amount
    print(f"充值成功！当前余额：{balance}元")

print("""===== 购物车系统 =====
当前余额：50元

商品列表：
苹果: 5元
香蕉: 3元
橙子: 4元
牛奶: 8元
面包: 6元

1. 显示商品
2. 添加商品到购物车
3. 查看购物车
4. 移除商品
5. 结算
6. 充值
7. 退出
""")
while True:
    chose=int(input("请选择："))
    if chose==1:
        show_products()
    elif chose==2:
        product_name = input("请输入商品名称：")
        add_to_cart(product_name)
    elif chose==3:
        show_cart()
    elif chose==4:
        product_name = input("请输入商品名称：")
        remove_from_cart(product_name)
    elif chose==5:
        checkout()
    elif chose==6:
        amount = int(input("请输入充值金额："))
        recharge(amount)
    elif chose==7:
        print("感谢光临！")
        break
    else:
        print("无效选择，请重新输入")