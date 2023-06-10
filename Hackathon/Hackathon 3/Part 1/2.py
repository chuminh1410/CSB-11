import math


def cal_area(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Input radius: "))
area = cal_area(radius)
print("Circle's area:", round(area,2))
