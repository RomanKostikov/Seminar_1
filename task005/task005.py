# 5. Напишите программу, которая принимает на вход число и проверяет,
# кратно ли оно 5 и 10 или 15, но не 30.
"""Doc."""
# первый вариант решения
num: int = int(input("введите число: "))
x = False
if (num % 5 == 0 and num % 10 == 0 or num % 15 == 0) and num % 30 != 0:
    x = True
print(x)

# второй вариант решения(на паре решили)
# n = int(input('Enter N: '))
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print('yes')
# else:
#     print('no')
