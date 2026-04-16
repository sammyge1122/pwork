
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def convert_temperature(value, unit='C'):
    if unit == 'C':
        result = celsius_to_fahrenheit(value)
        print(f"{value}°C = {result:.2f}°F")
    elif unit == 'F':
        result = fahrenheit_to_celsius(value)
        print(f"{value}°F = {result:.2f}°C")


print("===== 温度转换器 =====\n")
print("使用位置参数：convert_temperature(100, 'C')")
convert_temperature(100, 'C')
print("\n使用关键字参数：convert_temperature(value=32, unit='F')")
convert_temperature(value=32, unit='F')
print("\n使用默认参数：convert_temperature(37)")
convert_temperature(37)



