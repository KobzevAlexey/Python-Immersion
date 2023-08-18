class BankAccount:
    def __init__(self):
        self.transactions = []
        self.balance = 0

    def deposit(self, amount):
        if self.balance + amount > 5000000:
            wealth_tax = (self.balance + amount) * 0.1
            self.balance += (amount - wealth_tax)
            self.transactions.append(f"Депозит: +{amount} (Удержан налог на состояние: -{wealth_tax})")
        else:
            self.balance += amount
            self.transactions.append(f"Депозит: +{amount}")

        if len(self.transactions) % 3 == 0:
            self.charge_interest()

    def withdraw(self, amount):
        if self.balance > 5000000:
            wealth_tax = self.balance * 0.1
            self.balance -= wealth_tax

        if amount <= self.balance:
            withdrawal_fee = max(30, min(amount * 0.015, 600))
            self.balance -= (amount + withdrawal_fee)
            self.transactions.append(f"Вывод средств: -{amount} (Комиссия: -{withdrawal_fee})")

            if len(self.transactions) % 3 == 0:
                self.charge_interest()
        else:
            print("Недостаточно средств.")

    def charge_interest(self):
        interest = self.balance * 0.03
        self.transactions.append(f"Начисленный процент: +{interest}")

    def display_transactions(self):
        for transaction in self.transactions:
            print(transaction)

    def show_balance(self):
        print(self.balance)


def main():
    account = BankAccount()

    while True:
        print("\nМеню:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Показать историю")
        print("4. Показать баланс")
        print("5. Выход")

        choice = input("Выберите операцию (1-5): ")

        if choice == "1":
            amount = int(input("Введите сумму вклада (кратную 50): "))
            if amount % 50 == 0:
                account.deposit(amount)
            else:
                print("Неверная сумма вклада. Сумма должна быть кратна 50.")
        elif choice == "2":
            amount = int(input("Введите сумму вывода средств (кратно 50): "))
            if amount % 50 == 0:
                account.withdraw(amount)
            else:
                print("Неверная сумма вывода средств. Сумма должна быть кратна 50.")
        elif choice == "3":
            account.display_transactions()
        elif choice == "4":
            account.show_balance()
        elif choice == "5":
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте еще раз.')


if __name__ == "__main__":
    main()
