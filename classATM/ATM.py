class ATM:
    def __init__(self, balance=0):
        """
        初始化ATM对象，设置初始余额
        :param balance: 初始余额，默认为0
        """
        self.balance = balance

    def check_balance(self):
        """
        查询当前余额
        :return: 当前余额
        """
        return self.balance

    def deposit(self, amount):
        """
        存款操作
        :param amount: 存款金额
        :return: 存款后的余额
        """
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            return "存款金额必须大于0"

    def withdraw(self, amount):
        """
        取款操作
        :param amount: 取款金额
        :return: 取款后的余额或错误信息
        """
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                return "余额不足，无法取款"
        else:
            return "取款金额必须大于0"

    def __str__(self):
        """
        返回ATM对象的字符串表示
        :return: 当前余额的字符串形式
        """
        return f"当前余额: {self.balance}"

# 测试ATM程序
if __name__ == "__main__":
    atm = ATM(1000)  # 创建一个初始余额为1000的ATM对象
    print(atm)  # 输出当前余额

    print("存款500元")
    atm.deposit(500)
    print(atm)  # 输出存款后的余额

    print("取款200元")
    atm.withdraw(200)
    print(atm)  # 输出取款后的余额

    print("尝试取款1500元")
    print(atm.withdraw(1500))  # 输出取款失败的提示信息