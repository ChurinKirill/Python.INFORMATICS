a, b = map(int, input("Введите стороны прямоугольника ABCD - AB(CD), BC(AD): ").split())
square = a == b
if square:
    print(f"Это квадрат")
print(f"Площадь: S = AB * BC = {a} * {b} = {a * b}")
print("Периметр: ", end="")
if square:
    print(f"S = 4AB = {a} * 4 = {a * 4}")
else:
    print(f"S = 2(AB + BC) = 2({a} + {b}) = {2 * (a + b)}")
