while 1:
    a=input("请输入一个字符（输入quit退出）：")
    if a=="quit":
        break
    print(f"字符：{a}")
    print(f"Unicode码点：{ord(a)}")
    a=a.encode("utf-8")
    utf8_hex = ''.join([f'\\x{b:02x}' for b in a])
    print("UTF-8编码：%s"%(utf8_hex))
    a=a.decode("utf-8")
    a=a.encode("gbk")
    gbk_hex = ''.join([f'\\x{b:02x}' for b in a])
    print("GBK编码：%s"%(gbk_hex))
    a=a.decode("gbk")
    if ord(a)<128:
        print(f"备注：属于ASCII字符")