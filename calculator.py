import math


#Функция сложения двух чисел
def add(x, y):
    return x + y

#Функция вычитания двух чисел
def subtract(x, y):
    return x - y

#Функция умножения двух чисел
def multiply(x, y):
    return x * y

#Функция целочисленного деления первого операнда на второй
def integer_division(x, y):
    if y != 0:
        return x // y
    else:
        return "Error! Division by zero."

#Функция нахождения квадратного корня числа
def find_root(val):
    if val < 0:
        return f"Error! {val} is negative number."
    else:
        return val * 0.5 # Ошибка

#Функция нахождения логарифма первого операнда по основанию второго
def logarithm(x, base=math.e):
    if x <= 0:
        return f'Error! {x} < = 0.'
    if base <= 0 or base == 1:
        return "Error! {base} <= 0 or {base} == 1."
    return math.log(x, base)

print(find_root(81))
print(find_root(169))
print(find_root(64))
print(logarithm(81, 9))
