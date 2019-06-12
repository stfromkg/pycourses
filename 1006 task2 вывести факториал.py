#  сам не делал, нашел в интернете
n = int(input("введите число: "))
factorial = 1
for i in range(2, n + 1):
    factorial *= i

print (factorial)