# Напишите программу, которая принимает на вход координаты двух точек и
# находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
"""Doc."""
import math

Ax = int(input("Enter a coordinate Ax: "))
Bx = int(input("Enter a coordinate Bx: "))
Ay = int(input("Enter a coordinate Ay: "))
By = int(input("Enter a coordinate By: "))

Distance = float(round(math.sqrt(pow((Bx - Ax), 2) + pow((By - Ay), 2)), 2))
print(f"The distance from point A to point B is {Distance}")
