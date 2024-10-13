from logging import setLogRecordFactory


class Account():
    def __init__(self, id, balance=0):
        self.id = id
        self.balance = balance

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print(f"Вы успещно пополнили балансю Сумма на счету = {self.balance}")

    def withdraw(self, money):
        if money > self.balance:
            print("недостаточно денег на счету")
        elif money <= self.balance:
            self.balance -= money
            print(f"Вы успешно сняли {money} рублей. Остаток на счете: {self.balance}")

    def all_balance(self):
        print(f"текущий баланс: {self.balance}")

man = Account(123123123, 600)

man.all_balance()
man.withdraw(450)
man.withdraw(800)
man.deposit(23000)





