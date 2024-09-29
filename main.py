import math
v= float(input("Введите обьём шара в куб. ед.: "))
r = ((3 * v) / (4 * math.pi)) ** (1 / 3)
print("Радиус шара: ", r)
