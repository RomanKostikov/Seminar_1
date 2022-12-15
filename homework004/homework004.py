# Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
"""Doc."""
quarterNumber = int(input("Enter quarter number: "))
if quarterNumber == 1:
    print("X > 0 and Y > 0")
elif quarterNumber == 2:
    print("X < 0 and Y > 0")
elif quarterNumber == 3:
    print("X < 0 and Y < 0")
elif quarterNumber == 4:
    print("X > 0 and Y < 0")
else:
    print("data entered incorrectly")
