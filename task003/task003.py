# **Задачи:**
# 1. Напишите программу, которая будет на вход принимать число N и
# выводить числа от -N до N
#     *Примеры:*
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
"""Doc."""
# первый вариант решения задачи
# num = int(input("Введите число N: "))
# for number in range(-num, num+1):
#     print(number, end=", ")
# второй вариант решения задачи
a = int(input('введите число N = '))
list = range(-a, a+1, 1)
print(*list)
# лайфхак от учителя
# word = 'python'
# print(*word)
# print(*word, sep='-', end=' ')
# print(*word, sep='-', end='\n')
# print(*word, sep='\n'
