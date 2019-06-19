# Пользователь вводит число, затем вводит арифметическую операцию (+ или - или * или /) затем ещё одно число. Ваша задача - написать функцию, вычисляющую данное выражение
# Пример:
# 3
# *
# 6
# Вывод:
# 18

while True:
    a=input("первое число: ")
    b=input("второе число: ")
    c=input("действие: ")
    if c =='/':
        if int(b) != 0:
            print(int(a) / int(b))
        else:
            print("0")
    if c =='*':
        if int(b) !=0:
            print(int(a) * int(b))
        else:
            print("0")
    if c == '+':
        if int(b) !=0:
            print(int(a) + int(b))
        else:
            print(int(a) + int(b))
    if c == '-':
        if int(b) != 0:
            print(int(a) - int(b))
        else:
            print(int(a) - int(b))
