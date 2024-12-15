# Задание 1
# a = [1, 1, 2, 3, 5, 8, 10, 12, 34, 38, 40, 41, 46, 50, 55, 89]
# for i in a:
#     if i < 15:
#         print(i)

# Задание 2
# a = int(input("Введите число: "))

# if a == 0:
#     print("Число равняется нулю.")
# elif a > 0:
#     print("Число положительное")
# elif a < 0:
#     print("Число отрицательное ")

# Задание 3
# print("1. Умножение")
# print("2. Деление")
# print("3. Сложение")
# print("4. Вычитание")
# choose = int(input("Выберите действие над числом: "))
# if choose == 1:
#     a = int(input("Введите первое число для умножения: "))
#     b = int(input("Введите второе число для умножения: "))
#     print("Результат: " + str(a * b))
# elif choose == 2:
#     a = int(input("Введите первое число для деления: "))
#     b = int(input("Введите второе число для деления: "))
#     print("Результат: " + str(a / b))
# elif choose == 3:
#     a = int(input("Введите первое число для сложения: "))
#     b = int(input("Введите второе число для сложения: "))
#     print("Результат: " + str(a + b))
# elif choose == 4:
#     a = int(input("Введите первое число для вычитания: "))
#     b = int(input("Введите второе число для вычитания: "))
#     print("Результат: " + str(a - b))
# else:
#     print("Такого варианта не существует :( ") 

# Задание 4
# for i in range(11, 0, -1):
#     print(str(i - 1))

# Задание 5
import math

print("Уравнение: ax^2 + bx + c = 0")
a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))
c = int(input("Введите значение c: "))

if a == 0:
    print("Коэффициент a не может быть равен нулю для квадратного уравнения.")
else:
    d = b**2 - 4 * a * c
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print("Корни: " + str(x1) + " и " + str(x2))
    elif d == 0:
        x = -b / (2*a)
        print("Один корень: " + str(x))
    else:
        print("Нет действительных корней")