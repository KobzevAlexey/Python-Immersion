# Напишите программу банкомат. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной


transactions = []
balance = 0


def deposit(amount):
    global balance
    if balance + amount > 5000000:
        wealth_tax = (balance + amount) * 0.1
        balance += (amount - wealth_tax)
        transactions.append(f"Депозит: +{amount} (Удержан налог на состояние: -{wealth_tax})")
    else:
        balance += amount
        transactions.append(f"Депозит: +{amount}")
    if len(transactions) % 3 == 0:
        charge_interest()


def withdraw(amount):
    global balance
    if balance > 5000000:
        wealth_tax = balance * 0.1
        balance -= wealth_tax
    if amount <= balance:
        withdrawal_fee = max(30, min(amount * 0.015, 600))
        balance -= (amount + withdrawal_fee)
        transactions.append(f"Вывод средств: -{amount} (Комиссия: -{withdrawal_fee})")
        if len(transactions) % 3 == 0:
            charge_interest()
    else:
        print("Недостаточно средств.")


def charge_interest():
    global balance
    interest = balance * 0.03
    transactions.append(f"Начисленный процент: +{interest}")


def display_transactions():
    for transaction in transactions:
        print(transaction)


def show_balance():
    print(balance)


def main():
    while True:
        print("\nМеню:")
        print("1. Пополнить")
        print("2. Снять")
        print("3. Показать историю")
        print("4. Показать баланс")
        print("5. Выход")

        choice = input("Выберите операцию (1-5): ")

        if choice == "1":
            amount = int(input("Введите сумму вклада (кратную 50)): "))
            if amount % 50 == 0:
                deposit(amount)
            else:
                print("Неверная сумма вклада. Сумма должна быть кратна 50.")
        elif choice == "2":
            amount = int(input("Введите сумму вывода средств (кратно 50): "))
            if amount % 50 == 0:
                withdraw(amount)
            else:
                print("Неверная сумма вывода средств. Сумма должна быть кратна 50.")
        elif choice == "3":
            display_transactions()
        elif choice == "4":
            show_balance()
        elif choice == "5":
            break
        else:
            print('Неверный выбор. Пожалуйста, попробуйте еще раз.')


if __name__ == "__main__":
    main()
