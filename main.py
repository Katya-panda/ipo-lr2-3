import math
def calculate_radius(volume):
    radius = ((3 * volume) / (4 * math.pi)) ** (1 / 3)
    return radius
x = float(input("Введите объём шара в куб. ед.: "))
radius = calculate_radius(x)
print(f"Исковый радиус шара: {radius:.5f}")
