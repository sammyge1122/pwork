class TemperatureConverter:
    celsius_to_fahrenheit_count = 0
    fahrenheit_to_celsius_count = 0

    @staticmethod
    def celsius_to_fahrenheit(celsius):
        TemperatureConverter.celsius_to_fahrenheit_count += 1
        return celsius * 9 / 5 + 32

    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        TemperatureConverter.fahrenheit_to_celsius_count += 1
        return (fahrenheit - 32) * 5 / 9

    @classmethod
    def convert(cls, value, from_unit):
        if from_unit == 'C':
            return cls.celsius_to_fahrenheit(value)
        elif from_unit == 'F':
            return cls.fahrenheit_to_celsius(value)
        else:
            raise ValueError("单位必须是'C'或'F'")

    @classmethod
    def get_stats(cls):
        return f"摄氏度→华氏度转换次数：{cls.celsius_to_fahrenheit_count}\n华氏度→摄氏度转换次数：{cls.fahrenheit_to_celsius_count}"

    @classmethod
    def reset_stats(cls):
        cls.celsius_to_fahrenheit_count = 0
        cls.fahrenheit_to_celsius_count = 0

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def to_celsius(self):
        if self.unit == 'C':
            return self.value
        elif self.unit == 'F':
            return self.fahrenheit_to_celsius(self.value)
        else:
            raise ValueError("单位必须是'C'或'F'")

    def to_fahrenheit(self):
        if self.unit == 'C':
            return self.celsius_to_fahrenheit(self.value)
        elif self.unit == 'F':
            return self.value
        else:
            raise ValueError("单位必须是'C'或'F'")

    def __str__(self):
        return f"{self.value}°{self.unit}"
    
if __name__ == '__main__':
    print('===== 静态方法测试 =====')
    print(f"100°C = {TemperatureConverter.celsius_to_fahrenheit(100):.2f}°F")
    print(f"32°F = {TemperatureConverter.fahrenheit_to_celsius(32):.2f}°C\n")

    print('===== 类方法测试 =====')
    print(f"转换100°C到°F：{TemperatureConverter.convert(100, 'C'):.2f}°F")
    print(f"转换32°F到°C：{TemperatureConverter.convert(32, 'F'):.2f}°C\n")

    print('===== 统计信息 =====')
    print(TemperatureConverter.get_stats())

    print('===== 实例方法测试 =====')
    temp = TemperatureConverter(25, 'C')
    print(f"温度对象：{temp}")
    print(f"转换为华氏度：{temp.to_fahrenheit():.2f}°F")
    print(f"转换为摄氏度：{temp.to_celsius():.2f}°C\n")

    print('===== 重置统计 =====')
    TemperatureConverter.reset_stats()
    print(TemperatureConverter.get_stats())