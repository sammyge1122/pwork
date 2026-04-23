class Employee:
    employee_counter = 0
    all_employees = []


    def __init__(self, name, department, base_salary, bonus=0):
        self.__name = name#员工姓名
        Employee.employee_counter += 1
        self.__emp_id = f'E{Employee.employee_counter:03d}'#工号
        self.__department = department#部门
        self.__base_salary = base_salary#基本工资
        self.__bonus = bonus#奖金
        Employee.all_employees.append(self)

    @property
    def name(self):
        return self.__name

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def department(self):
        return self.__department

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    def bonus(self):
        return self.__bonus

    @property
    def total_salary(self):
        return self.__base_salary + self.__bonus

    @total_salary.setter
    def total_salary(self, value):#total_salary：总工资（基本工资+奖金），设置时会调整基本工资
        if value < self.__bonus:
            raise ValueError("总工资不能小于奖金")
        self.__base_salary = value - self.__bonus

    def promote(self, percent):#promote(percent)：加薪，基本工资增加百分比
        self.__base_salary += self.__base_salary * percent / 100
        print(f'{self.name}加薪{percent}%后，基本工资：{self.base_salary:.2f}')

    def give_bonus(self, amount):#give_bonus(amount)：发放奖金
        self.__bonus += amount
        print(f'{self.name}发放奖金{amount}元，当前总工资：{self.total_salary:.2f}')

    def info(self):#info()：返回员工详细信息
        return f'{self.name} - 工号：{self.emp_id} - 部门：{self.department} - 基本工资：{self.base_salary:.2f} - 奖金：{self.bonus:.2f} - 总工资：{self.total_salary:.2f}'
    


    @classmethod
    def get_employee_by_id(cls, emp_id):  #get_employee_by_id(emp_id)：根据工号查找员工
        for emp in cls.all_employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    @classmethod
    def get_employees_by_department(cls, department):#get_employees_by_department(department)：获取指定部门的所有员工
        return [emp for emp in cls.all_employees if emp.department == department]

    @classmethod
    def get_total_payroll(cls):#get_total_payroll()：计算所有员工的总工资
        return sum(emp.total_salary for emp in cls.all_employees)

    @classmethod
    def get_department_stats(cls):#get_department_stats()：统计每个部门的员工数和总工资
        stats = {}
        for emp in cls.all_employees:
            if emp.department not in stats:
                stats[emp.department] = {'count': 0, 'total_salary': 0}
            stats[emp.department]['count'] += 1
            stats[emp.department]['total_salary'] += emp.total_salary
        return stats
    
if __name__ == '__main__':
    print('===== 创建员工 =====')
    emp1 = Employee('张三', '技术部', 8000, 1000)
    emp2 = Employee('李四', '市场部', 7000, 500)
    emp3 = Employee('王五', '技术部', 9000, 2000)
    emp4 = Employee('赵六', '人事部', 6000, 300)
    for emp in Employee.all_employees:
        print(emp.info())
    print(f'员工总数：{Employee.employee_counter}\n')

    print('===== 工资统计 =====')
    print(f'所有员工总工资：{Employee.get_total_payroll():.2f}元\n')

    print('部门统计：')
    dept_stats = Employee.get_department_stats()
    for dept, stats in dept_stats.items():
        print(f'{dept}: {stats["count"]}人，总工资{stats["total_salary"]:.2f}元')
    
    print('\n===== 操作演示 =====')
    emp1.promote(10)
    emp1.give_bonus(2000)

    print('\n===== 查找员工 =====')
    emp = Employee.get_employee_by_id('E003')
    if emp:
        print(f'工号E003：{emp.name} - 部门：{emp.department} - 总工资：{emp.total_salary:.2f}')
    
    print('\n技术部员工：')
    tech_emps = Employee.get_employees_by_department('技术部')
    for emp in tech_emps:
        print(f'{emp.name} ({emp.emp_id}) - {emp.total_salary:.2f}元')