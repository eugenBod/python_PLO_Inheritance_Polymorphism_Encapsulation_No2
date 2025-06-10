class BankAccount:
    def __init__(self, initial_balance=0):
        self.__balance = initial_balance


    def get_balance(self):
        return self.__balance


    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено: {amount}руб.\nБаланс: {self.get_balance()}руб.")
        else:
            print("Сумма для пополнения счета должна быть больше ноля.")


    def withdrawal_money(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Снято: {amount}руб.\nБаланс: {self.get_balance()}руб.")
            else:
                print("Недостаточно средств на счете.")
        else:
            print("Сумма для снятия со счета должна быть больше ноля.")


account = BankAccount(100)
print(f"Текущий баланс: {account.get_balance()}руб.")
account.deposit(50)
account.deposit(-100)
account.withdrawal_money(60)
account.withdrawal_money(-100)
account.withdrawal_money(1000)
print(f"Текущий баланс: {account.get_balance()}руб.")