# monday = int(input("расход на пон: "))
# tuesday = int(input("расход на вт: "))
# wednesday = int(input("расход на ср: "))
# thursday = int(input("расход на чт: "))
# friday = int(input("расход на пт: "))
# saturday = int(input("расход на сб: "))
# sunday = int(input("расход на вс: "))
# expenses = monday + tuesday + wednesday + thursday + friday + saturday + sunday
# average = expenses/7
# print("расходы: ",expenses ,"ср.расходы: ", round(average,1))

def main():
    print("Добро пожаловать в программу подсчета расходов!")
    print("Введите ваши расходы за 7 дней.")

    expenses = []

    for day in range(1, 8):
        while True:
            try:
                expense = float(input(f"Введите расход за день {day}: "))
                expenses.append(expense)
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

    total_expenses = sum(expenses)
    print(f"Ваши общие расходы за неделю составляют: {total_expenses:.2f}")

if __name__ == "__main__":
    main()
