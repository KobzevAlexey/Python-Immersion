import datetime
import sys


# date_check запускается через консоль

def date_check(date: str) -> bool:
    try:
        datetime.datetime.strptime(date, '%d.%m.%Y')
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите дату в формате 'дд.мм.гггг'.")
        sys.exit(1)

    date_argument = sys.argv[1]
    if date_check(date_argument):
        print(f"Дата '{date_argument}' существует.")
    else:
        print(f"Даты '{date_argument}' не существует.")
