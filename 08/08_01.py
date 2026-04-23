class Student:
    def __init__(self, name, sid, score):
        self.name = name
        self.sid = sid
        self.score = score

    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 80:
            return 'B'
        elif self.score >= 70:
            return 'C'
        elif self.score >= 60:
            return 'D'
        else:
            return 'F'

    def info(self):
        return f'学号：{self.sid}，姓名：{self.name}，成绩：{self.score}，等级：{self.get_grade()}'

    def study(self, hours):
        old_score = self.score
        self.score = min(100, self.score + hours * 2)
        print(f'{self.name}学习了{hours}小时，成绩从{old_score}变为{self.score}')


if __name__ == '__main__':
    student1 = Student('张三', '1001', 85)
    student2 = Student('李四', '1002', 92)
    student3 = Student('王五', '1003', 58)
    print('===== 初始学生信息 =====')
    print(student1.info())
    print(student2.info())
    print(student3.info())
    print('\n===== 开始学习 =====')
    student1.study(2)
    student2.study(1)
    student3.study(4)
    print('\n===== 学习后学生信息 =====')
    print(student1.info())
    print(student2.info())
    print(student3.info())