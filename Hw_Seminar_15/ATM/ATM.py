import logging
import os

logging.basicConfig(level=logging.INFO, filename="bank_account.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')


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
            error_message = "Недостаточно средств для снятия {}. Баланс: {}".format(amount, self.balance)
            logging.error(error_message)
            print(error_message)

    def charge_interest(self):
        interest = self.balance * 0.03
        self.transactions.append(f"Начисленный процент: +{interest}")

    def display_transactions(self):
        if len(self.transactions) == 0:
            logging.info("История транзакций пуста.")
            print("История транзакций пуста.")
        else:
            for transaction in self.transactions:
                print(transaction)

    def show_balance(self):
        print(f"Баланс: {self.balance}")


def main():
    # Check if the log file exists and is writable
    log_file = "bank_account.log"
    if not os.access(log_file, os.W_OK):
        error_message = f"Невозможно записать в файл журнала {log_file}. Проверьте разрешения."
        print(error_message)
        logging.error(error_message)
        return

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
                error_message = "Неверная сумма вклада. Сумма должна быть кратна 50."
                logging.error(error_message)
                print(error_message)
        elif choice == "2":
            amount = int(input("Введите сумму вывода средств (кратную 50): "))
            if amount % 50 == 0:
                account.withdraw(amount)
            else:
                error_message = "Неверная сумма вывода средств. Сумма должна быть кратна 50."
                logging.error(error_message)
                print(error_message)
        elif choice == "3":
            account.display_transactions()
        elif choice == "4":
            account.show_balance()
        elif choice == "5":
            break
        else:
            error_message = "Неверный выбор операции."
            logging.error(error_message)
            print("Неверный выбор. Пожалуйста, попробуйте еще раз.")


if __name__ == "__main__":
    main()
