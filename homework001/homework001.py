# Напишите программу, которая принимает на вход цифру, обозначающую день
# недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
"""Doc."""
num = int(input("Enter a number: "))
if 1 <= num <= 5:
    print("no")
elif 6 <= num <= 7:
    print("yes")
else:
    print("data entered incorrectly")
