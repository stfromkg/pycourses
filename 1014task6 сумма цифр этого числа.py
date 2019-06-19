#Пользователь вводит число. Найти сумму цифр этого числа


num = int(input("Введите число: "))
sum = 0
while num > 0:
    d = num % 10
    num = num // 10
    sum += d
print("Сумма: ", sum)
