"""Doc."""

# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.
#     *Примеры:*
#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

num1 = int(input("Введите число 1: "))
num2 = int(input("Введите число 2: "))

if num1 == num2**2 or num2 == num1**2:
    print("да")
else:
    print("нет")
