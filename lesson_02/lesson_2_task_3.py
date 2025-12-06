import math
num_items = int(input("Введите сторону квадрата: "))

def square(side):
    area = side * side
    return math.ceil(area)

print(f"Площадь квадрата равна: {square(num_items)}")
