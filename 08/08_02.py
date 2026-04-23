class BankAccount:
    account_counter = 0

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance
        BankAccount.account_counter += 1
        self.__account_no = f'ACC{1000 + BankAccount.account_counter}'
        print(f'{self.owner}创建账户成功，账号：{self.__account_no}')

    @property
    def balance(self):
        return self.__balance

    @property
    def account_no(self):
        return self.__account_no

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'{self.owner}存入{amount}元，当前余额{self.__balance}元')
        else:
            print('存款金额必须大于0')

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f'{self.owner}取出{amount}元，当前余额{self.__balance}元')
            else:
                print('余额不足')
        else:
            print('取款金额必须大于0')

    def transfer(self, target_account, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.withdraw(amount)
                target_account.deposit(amount)
                print(f'转账成功！{self.owner}余额：{self.__balance}元，{target_account.owner}余额：{target_account.balance}元')
            else:
                print('余额不足，无法转账')
        else:
            print('转账金额必须大于0')

    def info(self):
        return f'{self.owner} - 账号：{self.account_no}，余额：{self.balance}元'
    
if __name__ == '__main__':
    print('===== 创建账户 =====')
    account1 = BankAccount('张三')
    account2 = BankAccount('李四')
    print(f'总账户数：{BankAccount.account_counter}\n')

    print('===== 存款操作 =====')
    account1.deposit(1000)
    account2.deposit(500)
    print()

    print('===== 取款操作 =====')
    account1.withdraw(300)
    account2.withdraw(600)
    print()

    print('===== 转账操作 =====')
    account1.transfer(account2, 200)
    print()

    print('===== 账户信息 =====')
    print(account1.info())
    print(account2.info())