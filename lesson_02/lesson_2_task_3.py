import math
num_items = float(input("Введите сторону квадрата: "))

def square(side):
    area = side * side
    return math.ceil(area)

print(f"Площадь квадрата равна: {square(num_items)}")
